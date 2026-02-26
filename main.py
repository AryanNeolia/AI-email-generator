from fastapi import FastAPI
from pydantic import BaseModel 
from openai import OpenAI
import os 
from dotenv import load_dotenv

load_dotenv()
app= FastAPI()


client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
class EmailRequest(BaseModel):
    message: str
    tone: str


api_key = os.getenv("OPENAI_API_KEY")

print("RAW KEY:", api_key)
print("REPR KEY:", repr(api_key))
print("KEY LENGTH:", len(api_key) if api_key else None)

client = OpenAI(api_key=api_key)

tone_map={
    "polite":"very polite and respectful",
    "assertive":"clear,confident and assertive",
    "professional":"formal and professional",
    "friendly":"warm but professional"
}


@app.post("/generate-email")
def generate_email(request: EmailRequest):
    selected_tone= tone_map.get(request.tone.lower(),"professional")
    prompt = f"""
Convert the following rough message into a {selected_tone} email.

Add:
-proper greetings
-Structured body 
-professional closing
-don't sound robotic
-give proper closure with regards

Message:
{request.message}
"""
    
    response=client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role":"user","content":prompt}
        ]
    )
    return{"generated_email":response.choices[0].message.content}


