import os
import uuid
from importlib.util import find_spec

import django
from django.core.wsgi import get_wsgi_application
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.wsgi import WSGIMiddleware
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel, ConfigDict

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
django.setup()

from polls.models import TodoTask  # noqa E402

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


class TodoTaskBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    title: str
    status: str = TodoTask.StatusChoices.NOT_STARTED


class TodoTaskCreate(TodoTaskBase):
    pass


class TodoTaskResponse(TodoTaskBase):
    id: uuid.UUID

    class Config:
        orm_mode = True


# Routes


@app.post("/tasks/", response_model=TodoTaskResponse)
def create_task(task: TodoTaskCreate):
    todo_task = TodoTask.objects.create(
        title=task.title,
        status=task.status,
    )
    return TodoTaskResponse.model_validate(todo_task)


@app.get("/tasks/", response_model=list[TodoTaskResponse])
def list_tasks():
    tasks = TodoTask.objects.all()
    return [TodoTaskResponse.from_orm(task) for task in tasks]


@app.get("/tasks/{task_id}/", response_model=TodoTaskResponse)
def retrieve_task(task_id: uuid.UUID):
    try:
        task = TodoTask.objects.get(id=task_id)
        return TodoTaskResponse.model_validate(task)
    except TodoTask.DoesNotExist:
        raise HTTPException(status_code=404, detail="Task not found")


@app.patch("/tasks/{task_id}/", response_model=TodoTaskResponse)
def patch_task(task_id: uuid.UUID, updates: TodoTaskBase):
    try:
        task = TodoTask.objects.get(id=task_id)
        if updates.title is not None:
            task.title = updates.title
        if updates.status is not None:
            task.status = updates.status
        task.save()
        return TodoTaskResponse.model_validate(task)
    except TodoTask.DoesNotExist:
        raise HTTPException(status_code=404, detail="Task not found")


@app.delete("/tasks/{task_id}/", response_model=dict)
def delete_task(task_id: uuid.UUID):
    try:
        task = TodoTask.objects.get(id=task_id)
        task.delete()
        return {"message": "Task deleted successfully"}
    except TodoTask.DoesNotExist:
        raise HTTPException(status_code=404, detail="Task not found")
