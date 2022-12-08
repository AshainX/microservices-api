from fastapi import FastAPI
from redis_om import get_redis_connection
from redis_om import HashModel

app = FastAPI()

redis = get_redis_connection(
    host="redis-14081.c301.ap-south-1-1.ec2.cloud.redislabs.com",
    port=14081,
    password="NpX1njzFhOgKBiUdHOUSuwvjouVvKAtX",
    decode_response=True
    
    
)

class Product(HashModel):
    name: str
    price: float
    quantity: int

    class Meta:
        database = redis

@app.get("/")
async def root():
    return {"message": "Hello World"}



    
