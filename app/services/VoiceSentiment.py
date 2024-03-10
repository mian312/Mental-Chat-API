import speech_recognition as sr

# Function to convert audio to text
def Speech_Recognition(audio):
    recognizer = sr.Recognizer()
    text = ""

    try:
        text = recognizer.recognize_google(audio, language="en-US")
        return format(text)
    except sr.UnknownValueError:
        return "Voice not recognized."
    except sr.RequestError:
        return "Could not connect to the speech recognition service."
