import sqlite3
import json

conn = sqlite3.connect('reloop.db')
cursor = conn.cursor()

# ---------- PRODUCTS ----------
cursor.execute("SELECT * FROM products")
products_rows = cursor.fetchall()

products = []
for row in products_rows:
    products.append({
        "prod_id": row[0],
        "prod_type": row[1],
        "days_left": row[2],
        "description": row[3]
    })

# ---------- STATUS ----------
cursor.execute("SELECT type, content FROM status")
status_rows = cursor.fetchall()

status = {
    row[0]: row[1].split(", ") if row[1] else []
    for row in status_rows
}

# ---------- FINAL JSON ----------
final_output = {
    "products": products,
    "status": status
}

# Save to file
with open("db_scripts/db_output.json", "w") as f:
    json.dump(final_output, f, indent=4)

print("JSON file created: db_output.json")