from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def Text_Sentiment(text):
    try:
        Sentence = [str(text)] # if taken the text directly then each character differently will be analyzed, so we need to convert it into a list
        analyzer = SentimentIntensityAnalyzer()

        for i in Sentence:
            sentiment = analyzer.polarity_scores(i)
            response = {
                "text": i,
                "sentiment": sentiment
            }
            return response
    except Exception as e:
        return {
            "error": str(e),
            "text": "Error in analyzing the text. Please try again."
        }



