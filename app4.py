"""
- 멀티턴 방식을 선택하는 기준
  - 프로그램에서 개입이 필요한지의 여부
    1. 프로그램에서 개입 불필요(ChatSession)
    2. 프로그램에서 개입 필요(파이썬에서 자체 관리)

- 비용에 관한 부분
  - token(입력, 출력)
  - 예: 응답 메세지 길이가 40글자 이내로 맞춰야 하는 상황
    - a: 손흥민 선수에 대해서 두 줄로 설명하세요.
    - b: 인공지능에 대해 한 문장으로 설명하시요.
"""

import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("API_KEY")

genai.configure(api_key=api_key)

model = genai.GenerativeModel('gemini-1.5-flash')

user_queries = [
    {"role": 'user', 'parts': ['인공지능에 대해 40자 이내의 문장으로 설명하세요.']},
    {"role": 'user', 'parts': ['의식이 있는지, 40자 이내의 문장으로 답하세요.']}
]

history = []    # 대화 내역 초기화

for user_query in user_queries:
    history.append(user_query)
    print(f"[사용자]: {user_query["parts"][0]}")
    response = model.generate_content(history)

    # 응답의 길이가 40자를 초과하는 경우 재실행
    while len(response.text) > 50:
        print(f"응답 메시지 길이: {len(response.text)}")
        response = model.generate_content(history)

    print(f"[Gemini]: {response.text}")
    history.append(response.candidates[0].content)

print("[History] 변수에 들어있는 값은 이렇습니다.")
print(history)


