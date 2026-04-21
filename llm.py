import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

api_key = os.GROQ_API_KEY

def llm(message):
    client = Groq(api_key)

    response = client.chat.completions.create(
        model="llama3-70b-8192"
        )

    return response.choices[0].message.content