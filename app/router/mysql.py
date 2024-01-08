import configparser
from http import server
import pymysql as mysql
from fastapi import APIRouter, Request
from app.db.mysql_connector import MYSQL

config = configparser.ConfigParser()
config.read('config.ini')

db = MYSQL()

mysql = APIRouter(prefix='/db/mysql')

@mysql.post('/GetServerInfo')
async def get_server_info(request: Request):
    server_info = {
        'channel_code' : '-1'
    }
    try:
        req = await request.json()
        hostname = req['hostname']
        query = f'''
                    select ChannelCode
                    from tb_Server_Info
                    where ServerName = '{hostname}'
                '''
        result, data = db.select(query)
        if result:
            data = data.one_or_one()

            channel_cdoe = data[0]

            server_info = {
                'channel_code' : f'{channel_cdoe}'
            }
    except Exception as e:
        print(e)

    return server_info