from prompts import ManualView_Expired_system_prompt
from prompts import ManualView_user_prompt
from llm import llm

def repurposes():
    messages = [
    {"role": "system", "content": ManualView_Expired_system_prompt},
    {"role": "user", "content": ManualView_user_prompt}
    ]

    str = llm(messages)
    return str