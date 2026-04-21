from prompts import ManualView_Expired_system_prompt,ManualView_user_prompt
from llm import llm
from db import days_left, prod_type, desc, present_list, expired_list

def repurposes():
    descp = desc.strip() if desc else "No specific description provided"
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