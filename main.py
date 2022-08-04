import uvicorn
from fastapi import FastAPI

from widgets import app as widgets

app = FastAPI()
app.include_router(widgets.router)


@app.get("/")
async def root():
    return {"message": "Welcome to Ankur's widgets API"}


def start():
    uvicorn.run("main:app", host="0.0.0.0", reload=True, workers=2)


if __name__ == "__main__":
    start()
