from .GeminiBot import Gemini_Bot


def chatbot(question, history):
    return Gemini_Bot(question, history)
