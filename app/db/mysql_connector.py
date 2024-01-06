import configparser
import pymysql as mysql
from fastapi import APIRouter

config = configparser.ConfigParser()
config.read('config.ini')



class Mysql():
    def __init__(self, logger) -> None:
        self.db = mysql.connect(
                        host=config['DMP_MYSQL']['host'],
                        user=config['DMP_MYSQL']['user'],
                        password=config['DMP_MYSQL']['password'],
                        db=config['DMP_MYSQL']['db'],
                        charset='utf8'
                    )

        self.cursor = self.db.cursor()
        self.logger = logger

    def select(self, query):
        result = []
        try:
            self.cursor.execute(query)
            rows = self.cursor.fetchall()

            for row in rows:
                result.append(row[0])

        except Exception as e:
            self.logger.error(e)
            print(e)

        return result

    def db_close(self):
        self.db.close()