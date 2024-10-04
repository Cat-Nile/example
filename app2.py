import os
import google.generativeai as genai

from dotenv import load_dotenv

load_dotenv()


api_key = os.getenv("API_KEY")

genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-1.5-flash")

"""
- 멀티턴 방식

[사용자]: 인공지능에 대해 한 문장으로 짧게 설명하세요.
[인공지능]: 인공지능은 컴퓨터가 인간과 유사하게 생각하고 학습하고 문제를 해결할 수 있도록 설계된 
기술입니다. 
[사용자]: 의식이 있는지 한 문장으로 답하세요.
[인공지능]: 아니요, 인공지능은 의식이 없습니다.

- python - Django 프레임워크
session = ""

- Gemini
ChatSession 객체

"""

chat_session = model.start_chat(history=[])

user_queries = ["인공지능에 대해 한 문장으로 짧게 설명하시오.", "의식이 있는지 없는지 한 문장으로 답하세요."]


# for i in range(10):
#     print(i)

for user_query in user_queries:
    print(f"[사용자]: {user_query}")
    response = chat_session.send_message(user_query)
    print(f"[Gemini]: {response.text}")

