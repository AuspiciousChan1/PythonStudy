import pymysql

from utils import output


class MySQLHandler:
    __db: pymysql.connections.Connection
    __cursor: object

    def __init__(self, host: str, user: str, password: str, database: str):
        self.__db = pymysql.connect(host, user, password, database)
        self.__cursor = self.__db.cursor()

    def __init__(self, database: str):
        self.__db = pymysql.connect("localhost", "root", "123456", database)
        self.__cursor = self.__db.cursor()

    def __del__(self):
        self.__cursor.close()

    def insert_into(self, inf: dict, table: str):
        key_str = output.sprint(inf.keys(), ", ")
        value_str = output.sprint(inf.values(), ", ")

        cmd = """INSERT INTO %s
                (%s)
                VALUES (%s)
              """ % (table, key_str, value_str)

        try:
            self.__cursor.execute(cmd)
            self.__db.commit()
        except:
            self.__db.rollback()


d = {}
for i in range(1000):
    s = "i%d" % i
    d[s] = i

print(d.keys())
print(d.values())
