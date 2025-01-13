# 开发人员  ：  ZhangDuoKuo
# 开发时间  ：  2024/6/28  15:47
# 文件名称  :  UserMangager.PY
# 开发工具  :  PyCharm
import sqlite3


class UserManager(object):
    def __init__(self):
        db_path = 'mys_database.db'  # 当前工作目录下创建或使用名为mydatabase.db的数据库文件
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                username TEXT NOT NULL,
                password INTEGER NOT NULL
            )
        ''')
        self.conn.commit()
    def add_user_info(self,username,password):
        try:
            self.cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
            self.conn.commit()
            return 0
        except Exception as e:
            return 1
    def search_user_info(self,username,password):
        try:
            self.cursor.execute("SELECT * FROM users WHERE username = ? and password = ?", (username, password))
            student = self.cursor.fetchone()
            if student:
                return 0
            else:
                return 2
        except Exception as e:
            return 1

