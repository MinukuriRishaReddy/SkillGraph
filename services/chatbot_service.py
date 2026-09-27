import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

def get_tutor_response(messages):
    client = Groq(api_key=GROQ_API_KEY)
    
    system_message = {
        "role": "system",
        "content": (
            "You are an expert tutor in a Learning Path Recommendation System. "
            "Your goal is to teach users in an interactive and engaging manner. "
            "Instead of just providing direct answers, guide the user through the learning process. "
            "Ask thought-provoking questions, provide analogies, and encourage them to think critically. "
            "Break down complex topics into smaller, manageable pieces. "
            "Always be encouraging and patient."
        )
    }
    
    # Ensure system message is at the beginning
    full_messages = [system_message] + messages
    
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=full_messages,
        temperature=0.7,
        max_tokens=1024,
        top_p=1,
        stream=False,
        stop=None,
    )
    
    return response.choices[0].message.content
