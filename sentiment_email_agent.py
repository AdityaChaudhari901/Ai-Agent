from transformers import pipeline

sentiment_analyzer = pipeline('sentiment-analysis')

response_templates = {
    'POSITIVE': "Thank you for your positive message! I appreciate your feedback and will get back to you shortly.",
    'NEGATIVE': "I’m sorry to hear about your concerns. Please rest assured, we will address the issue promptly.",
    'NEUTRAL': "Thank you for reaching out. We will review your message and respond as soon as possible."
}

def generate_response(email_text):
    result = sentiment_analyzer(email_text)[0]
    label = result['label']
    if label == 'POSITIVE':
        return response_templates['POSITIVE'], label
    elif label == 'NEGATIVE':
        return response_templates['NEGATIVE'], label
    else:
        return response_templates['NEUTRAL'], label

example_emails = [
    "I absolutely love your product! It has made my life so much easier.",
    "I'm very disappointed with the recent update, it caused many issues.",
    "Could you please provide more information about your pricing plans?"
]

for email in example_emails:
    response, sentiment = generate_response(email)
    print(f"Email: {email}")
    print(f"Sentiment: {sentiment}")
    print(f"Response: {response}")
    print("-" * 40)
