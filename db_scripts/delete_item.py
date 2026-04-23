import sqlite3

conn=sqlite3.connect('reloop.db')
cursor=conn.cursor()

from datetime import datetime
from db_scripts.product_fetch import specific_product

def delete(prod_id):
    row = specific_product(prod_id)

    if not row:
        print("Product not found")
        return

    product = row[0]

    print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - Delete item: {product} from DB? [y/n]")
    
    human = input().strip().lower()

    if human == 'y':
        cursor.execute("DELETE FROM products WHERE prod_id = ?", (prod_id,))
        conn.commit()
        print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - Deleted successfully")
    else:
        print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - Cancelling deletion")