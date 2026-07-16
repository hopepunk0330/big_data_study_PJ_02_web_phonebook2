from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

from database import Base, engine
from routers import auth, categories, contacts

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.mount("/static", StaticFiles(directory="../static"), name="static")

app.include_router(auth.router)
app.include_router(contacts.router)
app.include_router(categories.router)


@app.get("/")
def read_index():
    return FileResponse("../static/index.html")
