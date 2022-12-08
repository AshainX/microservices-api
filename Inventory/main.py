from fastapi import FastAPI
from redis_om import get_redis_connection
from fastapi.middleware.cors import CORSMiddleware
from redis_om import HashModel

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['http://127.0.0.1:8000'],
    allow_methods=['*'],
    
)

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

@app.get('/products')
def all():
    return Product.all_pks()



    
