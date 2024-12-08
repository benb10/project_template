from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()


# Allowlist the local frontend (http://localhost:3000)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


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
