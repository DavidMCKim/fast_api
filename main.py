# import click
# from core.config import config
from app.db import mysql_connector
import configparser
from fastapi import FastAPI
import os
import uvicorn

from pydantic import BaseModel

class Item(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None
    
dmp = FastAPI()

dmp.include_router(router=mysql_connector)

@dmp.post('/items/')
async def create_item(item: Item):
	return item

def main():
    uvicorn.run(
        app="main:dmp",
        host=config['APP']['host'],
        port=int(config['APP']['port']),
        reload=True
    )

if __name__ == "__main__":
    # 개읹어보 불러오기
    config = configparser.ConfigParser()
    config.read('config.ini')
    main()