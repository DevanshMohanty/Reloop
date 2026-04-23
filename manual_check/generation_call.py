import sqlite3
from prompts import ManualView_Present_system_prompt, ManualView_user_prompt,ManualView_Expired_system_prompt
from llm import llm

conn=sqlite3.connect('reloop.db')
cursor=conn.cursor()

def get_status():
    cursor.execute("""
    SELECT type, content FROM status
    """)

    rows = cursor.fetchall()

    status_dict = {row[0]: row[1] for row in rows}

    present_raw = status_dict.get("present", "")
    expired_raw = status_dict.get("expired", "")

    present_list = [p.strip() for p in present_raw.split(",") if p.strip()]
    expired_list = [e.strip() for e in expired_raw.split(",") if e.strip()]

    return present_list, expired_list

def uses(prod_type,days_left,description):
    present_list,expired_list=get_status()
    descp = description.strip() if description else "No specific description provided"
    present = ", ".join(present_list) if present_list else "None"
    expired = ", ".join(expired_list) if expired_list else "None"
    user_prompt = ManualView_user_prompt.format(
        days_left=days_left,
        product_type=prod_type,
        description=descp,
        present_list=present,
        expired_list=expired
    )

    messages = [
        {"role": "system", "content": ManualView_Present_system_prompt}, 
        {"role": "user", "content": user_prompt} 
    ]

    response = llm(messages)
    return response

def repurposes(prod_type,days_left,description):
    present_list,expired_list=get_status()
    descp = description.strip() if description else "No specific description provided"
    present = ", ".join(present_list) if present_list else "None"
    expired = ", ".join(expired_list) if expired_list else "None"
    user_prompt = ManualView_user_prompt.format(
        days_left=days_left,
        product_type=prod_type,
        description=descp,
        present_list=present,
        expired_list=expired
    )

    messages = [
        {"role": "system", "content": ManualView_Expired_system_prompt},
        {"role": "user", "content": user_prompt}
    ]

    response=llm(messages)
    return response