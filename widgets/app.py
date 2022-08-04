from typing import List, Optional

from fastapi import APIRouter, FastAPI, HTTPException
from prisma import Prisma
from prisma.models import Widget
from prisma.types import WidgetCreateInput, WidgetUpdateInput

app = FastAPI()
prisma = Prisma(auto_register=True)
router = APIRouter(prefix="/widgets", tags=["widgets"])


@router.get("/")
async def get_widgets() -> List[Widget]:
    # TODO: Include pagination and filtering
    return await Widget.prisma().find_many()


@router.get("/{id}")
async def get_widget(id: int) -> Widget:
    widget = await Widget.prisma().find_first(where={"id": id})

    if widget is None:
        raise HTTPException(status_code=404, detail="Widget not found.")

    return widget


@router.post("/")
async def post_widget(widget: WidgetCreateInput) -> Widget | HTTPException:
    if hasattr(widget, "id"):
        raise HTTPException(
            status_code=400, detail="You may not explicitly set an id."
        )

    return await Widget.prisma().create(widget)


@router.patch("/{id}")
async def update_widget(
    id: int, widget: WidgetUpdateInput
) -> Optional[Widget]:
    return await Widget.prisma().update(where={"id": id}, data=widget)


@router.delete("/{id}")
async def delete_widget(id: int):
    return await Widget.prisma().delete(where={"id": id})


@router.on_event("startup")
async def startup():
    await prisma.connect()


@router.on_event("shutdown")
async def shutdown():
    await prisma.disconnect()
