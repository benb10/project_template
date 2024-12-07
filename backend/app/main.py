from fastapi import FastAPI

from fastadmin import fastapi_app as admin_app
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()


# Allowlist the local frontend (http://localhost:3000)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Specify the frontend URL here
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)


app.mount("/admin", admin_app)


@app.get("/hello_world")
async def root():
    return {"message": "Hello World"}


class AddRequest(BaseModel):
    nums: list[int | float]


class AddResponse(BaseModel):
    result: int | float


@app.post("/add", response_model=AddResponse)
async def add(request: AddRequest):
    result = sum(request.nums)
    return AddResponse(result=result)
