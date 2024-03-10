from .TextSentiment import Text_Sentiment
from .VoiceSentiment import Speech_Recognition

# Path: app/services/__init__.py

# Recognize the input type (text, audio, image, video, unknown)
def recognize_input_type(input_data):
    if isinstance(input_data, str):
        return 'text'
    elif isinstance(input_data, bytes):
        return 'audio'
    elif isinstance(input_data, list):
        return 'image'
    else:
        return 'unknown'
    



# Analyze the input data and return the sentiment
def analyze_input(input_data):
    input_type = recognize_input_type(input_data)
    
    if input_type == 'text':
        return Text_Sentiment(input_data)
    elif input_type == 'audio':
        speech = Speech_Recognition(input_data)
        return Text_Sentiment(speech)
    else:
        return {
            "error": "Unsupported input type",
            "text": "The input type is not supported. Please try again."
        }
    