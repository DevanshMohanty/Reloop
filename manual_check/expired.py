from prompts import ManualView_Expired_system_prompt
from prompts import ManualView_user_prompt
from llm import llm

def repurposes():
    system_prompt = ManualView_Expired_system_prompt
    user_prompt = ManualView_user_prompt
    
    messages = [
    {"role": "system", "content": system_prompt},
    {"role": "user", "content": user_prompt}
    ]

    str = llm(messages)
    return str