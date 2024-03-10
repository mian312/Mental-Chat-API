from gradio_client import Client

client = Client("https://givyboy-mental-health-chatbot.hf.space/--replicas/04p3w/")

def Mental_Health_Bot(message):
    result = client.predict(
        message,  # str  in 'Message' Textbox component
        api_name="/chat"
    )
    return result

while True:
    question = input("Ask a question: ")
    if question == "exit":
        break
    response = Mental_Health_Bot(question)
    print(response)