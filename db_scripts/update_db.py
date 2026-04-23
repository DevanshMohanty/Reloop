import sqlite3
from datetime import datetime
import re

conn=sqlite3.connect('reloop.db')
cursor=conn.cursor()

def daily_update():
    flag = expiry_check()

    print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} -Updating days left")
    cursor.execute("""
        UPDATE products
        SET days_left = days_left - 1
    """)
    conn.commit()

    if flag:
        status_update()


def expiry_check():
    check = False

    cursor.execute("SELECT prod_id, days_left FROM products")
    rows = cursor.fetchall()
    print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} -Checking for expiration")
    for days_left in rows:
        if days_left == 0:
            check = True

    return check


def status_update():   
    #fetch all products
    cursor.execute("SELECT prod_id, days_left FROM products")
    rows = cursor.fetchall()

    present = []
    expired = []

    for prod_id, days_left in rows:
        if days_left < 0:
            expired.append(str(prod_id))
        else:
            present.append(str(prod_id))

    cursor.execute(
    "UPDATE status SET content=? WHERE type='present'",
    (",".join(present),)
    )

    cursor.execute(
        "UPDATE status SET content=? WHERE type='expired'",
        (",".join(expired),)
    )

    print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} -Changing the status table")
    conn.commit()

def attribute_update(prod_id,change,button):
    cursor.execute("SELECT prod_type,days_left,desc FROM products WHERE prod_id = ?",(prod_id))
    row = cursor.fetchall()

    if not row:
        print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - Row does not exist")
        return

    prod_type, old_days, desc = row

    change = change.strip()

    if button == 1:     #if the change is in days left
        new_days = int(change)

        cursor.execute(
            "UPDATE products SET days_left = ? WHERE prod_id = ?",
            (new_days, prod_id)
        )
        if (new_days*old_days) < 0:
            status_update()
        print(f"Updated days_left → {new_days}")

    elif button == 2:       #if the change is in description
        cursor.execute(
            "UPDATE products SET description = ? WHERE prod_id = ?",
            (change, prod_id)
        )
        print(f"Updated description → {change}")

    else: #if the change is in product_type 
        cursor.execute(
            "UPDATE products SET prod_type = ? WHERE prod_id = ?",
            (change, prod_id)
        )
        print(f"Updated prod_type → {change}")

    conn.commit()

