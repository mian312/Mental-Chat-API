import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load the environment variables
load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=API_KEY)

# Set up the model
generation_config = {
  "temperature": 0.2,
  "top_p": 1,
  "top_k": 1,
  "max_output_tokens": 512,
}

# Set up safety settings
safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_ONLY_HIGH"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_ONLY_HIGH"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_ONLY_HIGH"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_ONLY_HIGH"
  },
]

# Create the model
model = genai.GenerativeModel(model_name="gemini-1.0-pro",
                              generation_config=generation_config,
                              safety_settings=safety_settings)

# Giving context and instructions to the model
instructions = "You are a helpful mental health chatbot, who only talk to the point and always ask the user about their situation before answering them. (Your knowledge is limited to mental health only)."


# Exporting the model
def Gemini_Bot(question, history):
    convo = model.start_chat(history=history)
    response = convo.send_message(instructions + question)
    return response.text

# while True:
#     question = input("Ask a question: ")
#     if question == "exit":
#         break
#     response = Gemini_Bot(question)
#     print(response)
