# import uvicorn
from fastapi import FastAPI

app = FastAPI(
        title="Shot2shot API",
        description="From espresso shot to web",
        version="1.0.0"
)

@app.get("/")
def index():
  return {"Hello": "World"}


def start():
    """ Launched with `poetry run start` at the root level"""
    uvicorn.run("app.main:app", host="localhost", port=8888, reload=True)