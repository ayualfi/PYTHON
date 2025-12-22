import pymysql

class Database:
    def __init__(self):
        self.host = 'localhost'
        self.user = 'root'
        self.pwd = ''
        self.db = 'db_kasir_a'
    def get_connection(self):
        try:
            c = pymysql.connect(
                host= self.host,
                user=self.user,
                password=self.pwd,
                database=self.db
            )
            return c
        except:
            print('Koneksi basis data gagal')
            return False