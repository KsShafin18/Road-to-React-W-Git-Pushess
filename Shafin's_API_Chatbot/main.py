
import os
from google import genai
from dotenv import load_dotenv

# Load API key
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    print("Please add your Gemini API key to .env")
    exit()

# Create Gemini client
client = genai.Client(api_key=api_key)

# Start chat
chat = client.chats.create(
    model="gemini-3.8-flash"
)

print("\n Ks-GPT:")
print("Type 'exit' to quit.\n")

while True:
    question = input("You: ").strip()

    if question.lower() == "exit":
        print("Bot: Goodbye!")
        break

    if not question:
        continue

    try:
        response = chat.send_message(question)
        print("\nBot:", response.text, "\n")

    except Exception as error:
        print("Something went wrong:", error)


    #Notes
        # .env namer envioment banao pore oitay
        # GEMINI_API_KEY= pore nijer api dao
