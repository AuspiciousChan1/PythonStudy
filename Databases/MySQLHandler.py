import numpy
import pymysql

from utils import output


class MySQLHandler:
    __db: pymysql.connections.Connection
    __cursor: object

    def __init__(self, database: str, host="localhost", user="root", password="mysql81680396MYSQL"):
        self.__db = pymysql.connect(host, user, password, database)
        self.__cursor = self.__db.cursor()

    def __del__(self):
        self.__cursor.close()

    def insert_into(self, inf: dict, table: str):
        key_str = output.sprint(inf.keys(), ", ")
        value_str = output.sprint(inf.values(), ", ", True)

        cmd = """INSERT INTO %s
                (%s)
                VALUES (%s)
              """ % (table, key_str, value_str)
        try:
            self.__cursor.execute(cmd)
            self.__db.commit()
        except:
            print("error: insert fair")
            self.__db.rollback()

    def drop_table(self, table_name: str)->bool:
        try:
            cmd = "DROP TABLE %s" % table_name
            self.__cursor.execute(cmd)
            return True
        except pymysql.err.InternalError:
            return False

        # cmd = "DROP TABLE IF EXISTS %s" % table_name

    def create_table(self, table_name: str, column_inf: dict):
        # table_name: 新表的名称
        # column_inf: 新表的列信息，key记录列名称，value记录列限制条件，是Iterable的
        try:
            cmd = "CREATE TABLE %s(" % table_name
            for k in column_inf.keys():
                v = column_inf.get(k)
                separated_column_inf = ""
                for i in v:
                    separated_column_inf += str(i) + " "
                separated_column_inf = separated_column_inf[0: len(separated_column_inf)-1]
                cmd += "%s  %s, " % ( k, separated_column_inf)
            cmd = cmd[0: len(cmd) - 2] + ")"
            self.__cursor.execute(cmd)
            return True
        except pymysql.err.InternalError:
            print("fail: table %s has already existed" % table_name)
            return False
