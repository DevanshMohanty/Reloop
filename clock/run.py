import schedule
import time
from db_scripts.update_db import daily_update
from daily_check.main import daily_check
import sqlite3

conn=sqlite3.connect('reloop.db')
cursor=conn.cursor()



def job1():#only to update the sql database
    print("Updating DB")
    daily_update(time)
    
    
def job2():#only yields notifications
    print("Delivering Notifications")
    cursor.execute("SELECT prod_id, days_left FROM products")
    rows = cursor.fetchall()
    threshold = 3
    i = 1
    for days_left, prod_type in rows:
        notif = daily_check(threshold,days_left,prod_type)
        print(f"NOTIFICATION {i}")
        print(f'\n{notif}')
        i+=1
    

# Run at 12:00 AM every day
schedule.every().day.at("00:00").do(
    notif = job1
    )

# Run at 10:00 AM every day
schedule.every().day.at("10:00").do(job2)

while True:
    schedule.run_pending()
    time.sleep(1)