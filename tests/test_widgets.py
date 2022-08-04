import pytest
from httpx import AsyncClient

from main import app
from widgets.utils.seed_widgets import widgets_seed_data

# TODO: Seperate test db and live db


@pytest.fixture()
async def api_test_client():
    async with AsyncClient(app=app, base_url="http://test") as client:
        await app.router.startup()
        yield client
        await app.router.shutdown()


@pytest.mark.anyio
async def test_get_widgets(api_test_client: AsyncClient):
    res = await api_test_client.get("/widgets/")
    assert res.status_code == 200
    assert len(res.json()) == len(widgets_seed_data)


@pytest.mark.anyio
async def test_get_single_widget(api_test_client: AsyncClient):
    res = await api_test_client.get("/widgets/2")
    assert res.status_code == 200

    actual = res.json()
    expected = {
        "name": "w2",
        "parts": 2,
    }
    assert actual["name"] == expected["name"]
    assert actual["parts"] == expected["parts"]


@pytest.mark.anyio
async def test_create_and_delete_widget(api_test_client: AsyncClient):
    new_widget = {"name": "test widget", "parts": 200}
    res = await api_test_client.post("/widgets/", json=new_widget)

    actual = res.json()
    assert actual["name"] == new_widget["name"]
    assert actual["parts"] == new_widget["parts"]

    # now delete it
    res = await api_test_client.delete(f"/widgets/{actual['id']}")
    assert res.status_code == 200

    # check if it still exists
    res = await api_test_client.get(f"/widgets/{actual['id']}")
    assert res.status_code == 404


@pytest.mark.anyio
async def test_update(api_test_client: AsyncClient):
    res = await api_test_client.patch(
        "/widgets/3", json={"name": "i have been updated"}
    )
    assert res.status_code == 200

    res = await api_test_client.get("/widgets/3")
    assert res.status_code == 200
    assert res.json()["name"] == "i have been updated"

    res = await api_test_client.patch("/widgets/3", data={"name": "w3"})
