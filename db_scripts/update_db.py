import sqlite3

conn=sqlite3.connect('reloop.db')
cursor=conn.cursor()

def daily_update(time):
    flag = expiry_check()

    print(f"Updating days left at {time}")
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

    print('Changing the status table')
    conn.commit()
