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
