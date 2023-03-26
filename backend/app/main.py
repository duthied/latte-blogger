# import uvicorn
from fastapi import FastAPI
import uvicorn

app = FastAPI(
        title="Shot2shot API",
        description="From espresso shot to web",
        version="1.0.0"
)

@app.get("/")
def index():
  return {"Hello": "World"}

# def start():
#   uvicorn.run("app.main:app", host="localhost", port=8888, reload=True)