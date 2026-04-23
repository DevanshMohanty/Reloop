import sqlite3

conn=sqlite3.connect('reloop.db')
cursor=conn.cursor()


cursor.execute("DELETE FROM products")
cursor.executemany("""
INSERT INTO products (prod_type, days_left, description)
VALUES (?, ?, ?)
""", [
    ("Milk", 2, "Dairy product - keep refrigerated"),
    ("Bread", 1, "Whole wheat bread"),
    ("Cheese", -1, ""),
    ("Yogurt", -3, ""),
    ("Shampoo", 15, "Hair care product"),
    ("Face Cream", 30, "Skin moisturizer"),
    ("Butter", -2, ""),
    ("Eggs", 5, "Farm fresh eggs"),
    ("Juice", 0, ""),
    ("Soap", 50, "Bath soap")
])

# Present (>= 0)
cursor.execute("""
SELECT prod_type FROM products
WHERE days_left >= 0
""")
present = [row[0] for row in cursor.fetchall()]

# Expired (< 0)
cursor.execute("""
SELECT prod_type FROM products
WHERE days_left < 0
""")
expired = [row[0] for row in cursor.fetchall()]

present_str = ", ".join(present)
expired_str = ", ".join(expired)

cursor.execute("""
UPDATE status SET content = ?
WHERE type = ?
""", (present_str, "present"))

cursor.execute("""
UPDATE status SET content = ?
WHERE type = ?
""", (expired_str, "expired"))

conn.commit()