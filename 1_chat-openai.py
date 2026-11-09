"""1_chat-openai.py - de kleinste AI-call in Python (AI Impact Lab, sessie 4).

Zet je key in een .env bestand (zie .env.example) of: export OPENAI_API_KEY=...
Draai:  python 1_chat-openai.py
"""
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()          # leest OPENAI_API_KEY uit .env / je omgeving
client = OpenAI()      # pakt OPENAI_API_KEY automatisch op

stream = client.responses.create(
    model="gpt-6-luna",
    input=[
        {
            "role": "user",
            "content": "Write a bedtime story about the Netherlands winning the 2026 world cup.",
        },
    ],
    stream=True,
)

for event in stream:
    print(event)
