import configparser
import pymysql as mysql

config = configparser.ConfigParser()
config.read('config.ini')

class MYSQL():
    def __init__(self) -> None:
        self.db = mysql.connect(
                        host=config['DMP_MYSQL']['host'],
                        user=config['DMP_MYSQL']['user'],
                        password=config['DMP_MYSQL']['password'],
                        db=config['DMP_MYSQL']['db'],
                        charset='utf8'
                    )

        self.cursor = self.db.cursor()

    def select(self, query):
        result = []
        try:
            self.cursor.execute(query)
            rows = self.cursor.fetchall()

            for row in rows:
                result.append(row[0])

        except Exception as e:
            # self.logger.error(e)s
            print(e)

        return result

    def db_close(self):
        self.db.close()