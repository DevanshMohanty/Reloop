import sqlite3
import json
from pathlib import Path
from .generation_call import repurposes,uses


conn=sqlite3.connect('reloop.db')
cursor=conn.cursor()

base_dir=Path(__file__).resolve().parent
CACHE_FILE = base_dir / "llm_cache.json"

def normalize(text):
    if not text:
        return ""
    return " ".join(str(text).strip().lower().split())

def load_cache():
    if CACHE_FILE.exists():
        try:
            with open(CACHE_FILE, "r") as f:
                return json.load(f)
        except:
            return {}
    return {}

def save_cache(cache):
    CACHE_FILE.parent.mkdir(parents=True,exist_ok=True)
    with open(CACHE_FILE, "w") as f:
        json.dump(cache, f, indent=2)

cache=load_cache()

def manual_check(prod_type,days_left,prod_id,description):
    prod_id=str(prod_id)
    print(f"\nPRODUCT NAME: {prod_type}")
    status = 'Usable' if days_left>0 else 'Expired'
    print(f"\nPRODUCT STATUS: {status}")
    if prod_id in cache:
        cached=cache[prod_id]
        if cached.get("days_left")==days_left and normalize(description)==cached.get("description", "")  and cached.get("status")==status:
            print("\n[CACHE HIT]")
            print(f"\n{cached['output']}")
            return
        
    if status=="Expired":
        days_passed=-1*days_left
        print(f"\nDays Passed Since Expiry: {days_passed}")
        output = repurposes(prod_type,days_left,description)
    else:
        print(f"\nDays Left Until Expiry: {days_left}")
        output = uses(prod_type,days_left,description)

    print(f"\n{output}")

    cache[prod_id] = {
        "days_left": days_left,
        "description":normalize(description),
        "status":status,
        "prod_type": prod_type,
        "output": output
    }

    save_cache(cache)

target_prod_id=int(input("Enter the product id:"))
cursor.execute("""
Select prod_type,days_left,prod_id,description
FROM products
where prod_id=?
""",(target_prod_id,))

row = cursor.fetchone()
    
if row:
    manual_check(*row)
else:
    print(f"No product found with prod_id={target_prod_id}")
conn.close()