import os

from dotenv import load_dotenv

import google.generativeai as genai

load_dotenv()

api_key = os.getenv("API_KEY")

genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-1.5-flash")

"""
멀티턴 방식2 
- 대화 이력을 사용자 프로그램에서 직접 관리하는 형태

- dictionary
{
    'a': 1,
    'b': 2,
}

- list
[1, 2, 3, 4, 5]

"""




user_queries = [
    {'role': 'user', 'parts': ["인공지능에 대해 한 문장으로 설명하시오."]},
    {'role': 'user', 'parts': ["의식이 있는지 한 문장으로 답하세요."]}
]

# 대화내역 리스트 초기화
history = []

for user_query in user_queries:
    history.append(user_query)
    print(f"[사용자]: {user_query["parts"][0]}")
    response = model.generate_content(history)
    print(f"[Gemini]: {response.text}")
    history.append(response.candidates[0].content)

