from fastapi import FastAPI
from redis_om import get_redis_connection

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}



    
