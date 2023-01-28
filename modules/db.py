import sqlite3
class Database:
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute(
            "CREATE TABLE IF NOT EXISTS accounts (id INTEGER PRIMARY KEY, user text, password text)")
        self.conn.commit()
    def add(self,user,password):
        self.cur.execute("INSERT INTO accounts VALUES (NULL, ?, ?)",
                         (user,password))
        self.conn.commit()
    def fetch(self):
        self.cur.execute(f"SELECT * FROM accounts")
        rows = self.cur.fetchall()
        return rows
    def update(self):
        pass
    def remove(self):
        pass