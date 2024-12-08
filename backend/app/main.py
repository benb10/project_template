from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()


# Allowlist the local frontend (http://localhost:3000)
app.add_middleware(
    CORSMiddleware,
    # allow_origins=[
    #     "http://localhost:3000",  # local
    #     "https://project-template-beta.vercel.app",  # prod
    # ],
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health_check")
async def health_check():
    return {"message": "OK"}

@app.get("/version")
async def version():
    return {"version": "3"}

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
