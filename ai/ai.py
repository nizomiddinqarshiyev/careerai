import os
from dotenv import load_dotenv
from openai import OpenAI
from .models import Text

load_dotenv()
gpt_key = os.getenv("GPT_KEY")
MODEL = "gpt-3.5-turbo"  # yoki  "gpt-4o"byudjetga qarab

client = OpenAI(api_key=gpt_key)

def generate_gpt_response(user_message, system_field="system_text", text_field="prompt_text"):
    # Matnlarni modeldan olish
    system_text = Text.objects.values_list(system_field, flat=True).first() or ""
    prompt_text = Text.objects.values_list(text_field, flat=True).first() or ""

    # Xabarlar ketma-ketligi
    messages = [
        {
            "role": "system",
            "content": (
               f"{system_text}"
            )
        },
        {"role": "user", "content": f"{prompt_text}\n\n{user_message}"}
    ]

    # ChatGPT API orqali javob olish
    response = client.chat.completions.create(
        model=MODEL,
        messages=messages,
        temperature=0.5,
    )
    return response.choices[0].message.content


def chatbot_first(message):
    return generate_gpt_response(message, "system", "text")

def chatbot_second(message):
    return generate_gpt_response(message, "system", "text2")
