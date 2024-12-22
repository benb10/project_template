import os
from importlib.util import find_spec

from django.core.wsgi import get_wsgi_application
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.wsgi import WSGIMiddleware
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",  # local
        "https://project-template-beta.vercel.app",  # prod
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.mount(
    "/django/static/",
    StaticFiles(directory=os.path.normpath(os.path.join(find_spec("django.contrib.admin").origin, "..", "static"))),
    name="static",
)


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
application = get_wsgi_application()
app.mount("/django", WSGIMiddleware(application))


@app.get("/health_check")
async def health_check():
    return {"message": "OK"}


@app.get("/version")
async def version():
    return {"version": "3"}


@app.get("/hello_world")
def hello_world():
    from django.contrib.auth.models import User

    User.objects.create_superuser(username="a@a.com", email="a@a.com", password="Password1.")
    return {"message": "Hello World"}


@app.get("/hello_world2")
def hello_world2():
    return {"a": os.getenv("test")}


class AddRequest(BaseModel):
    nums: list[int | float]


class AddResponse(BaseModel):
    result: int | float


@app.post("/add", response_model=AddResponse)
async def add(request: AddRequest):
    result = sum(request.nums)
    return AddResponse(result=result)
