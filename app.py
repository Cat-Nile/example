import os

from dotenv import load_dotenv

load_dotenv()

# 싱글턴 방식 - 
import google.generativeai as genai

api_key = os.getenv("API_KEY")
genai.configure(api_key=api_key)

model = genai.GenerativeModel('gemini-1.5-flash')

response = model.generate_content("손흥민 선수에 대해서 두줄로 설명해주세요.")

print(f"답변: {response.text}")
