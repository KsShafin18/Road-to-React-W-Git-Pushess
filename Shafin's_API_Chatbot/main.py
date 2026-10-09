
import os
from dotenv import load_dotenv
from groq import Groq
from google import genai

load_dotenv()

# Provider change korlei AI change hobe
AI_PROVIDER = os.getenv("AI_PROVIDER", "groq").lower()


def ask_ai(question):
    if AI_PROVIDER == "groq":
        client = Groq(
            api_key=os.getenv("GROQ_API_KEY")
        )

        response = client.chat.completions.create(
            model="openai/gpt-oss-20b",
            messages=[
                {"role": "user", "content": question}
            ]
        )

        return response.choices[0].message.content

    elif AI_PROVIDER == "gemini":
        client = genai.Client(
            api_key=os.getenv("GEMINI_API_KEY")
        )

        response = client.models.generate_content(
            model="gemini-3.8-flash",
            contents=question
        )

        return response.text

    else:
        return "Unknown AI provider!"


print("🤖 ShafinGPT:Ask Here!")
print("Type 'exit' to stop.\n")

while True:
    question = input("You: ").strip()

    if question.lower() == "exit":
        break

    if not question:
        continue

    try:
        answer = ask_ai(question)
        print("\nBot:", answer, "\n")

    except Exception as error:
        print("\nError:", error, "\n")



        # attachments:

        # make a file name .env then add these 
        # AI_PROVIDER=groq

        # GROQ_API_KEY=
        # GEMINI_API_KEY=
