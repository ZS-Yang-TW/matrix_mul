from cloup import command
import pymysql
import datetime

class database():
    def __init__(self , parent = None):
        self.db_settings = {
            "host": "192.168.174.142",
            "port": 3306,
            "user": "root",
            "password": "123456789",
            "db": "edu_tech",
            "charset": "utf8"
        }

    def connect(self):
        self.conn = pymysql.connect(**self.db_settings)
        self.cursor = self.conn.cursor()

    def insert(self, data):
        data = data[2:-2].split("},{")
        self.conn = pymysql.connect(**self.db_settings)
        self.cursor = self.conn.cursor()
        command = "INSERT INTO test(time, 1st_row, 2nd_row, 3rd_row)VALUES(%s, %s, %s, %s)"
        self.cursor.execute(command, (datetime.datetime.now(), data[0], data[1], data[2]))
        self.conn.commit()
        self.conn.close()

    def select_last(self):
        self.conn = pymysql.connect(**self.db_settings)
        self.cursor = self.conn.cursor()
        command = "SELECT 1st_row, 2nd_row, 3rd_row FROM test order by id desc LIMIT 1"
        self.cursor.execute(command)
        result = self.cursor.fetchone()

        # command = "SELECT 2nd_row FROM test LIMIT 1"
        # self.cursor.execute(command)
        # result1 = self.cursor.fetchall()

        # command = "SELECT 3rd_row FROM test LIMIT 1"
        # self.cursor.execute(command)
        #result2 = self.cursor.fetchall()
        self.conn.commit()
        self.conn.close()
        
        #print(result)

        return result
