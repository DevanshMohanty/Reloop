import sqlite3

conn=sqlite3.connect('reloop.db')
cursor=conn.cursor()

cursor.execute("DROP TABLE IF EXISTS products")
cursor.execute("DROP TABLE IF EXISTS status")

#create products table
cursor.execute("""
CREATE TABLE IF NOT EXISTS products(
    prod_id INTEGER PRIMARY KEY AUTOINCREMENT,
    prod_type TEXT NOT NULL,
    days_left INTEGER NOT NULL,
    description TEXT
)
""")

#create status table
cursor.execute("""
CREATE TABLE IF NOT EXISTS status(
    type TEXT PRIMARY KEY,
    content TEXT
)
""")

cursor.execute("""
INSERT OR REPLACE INTO status (type, content)
VALUES (?, ?)
""", ("present", ""))

cursor.execute("""
INSERT OR REPLACE INTO status (type, content)
VALUES (?, ?)
""", ("expired", ""))

conn.commit()