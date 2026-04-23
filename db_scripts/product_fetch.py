import sqlite3

conn=sqlite3.connect('reloop.db')
cursor=conn.cursor()

from datetime import datetime

def specific_product(prod_id):
    cursor.execute("SELECT prod_type FROM products WHERE prod_id = ?", (prod_id))
    row = cursor.fetchone()
    return row

def all_products():
    cursor.execute("SELECT prod_id,prod_type,days_left FROM products")
    row = cursor.fetchone()
    return row