import nltk
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score

nltk.download('punkt')

def tokenize_input(input_text):
    return word_tokenize(input_text)

def classify_intent(input_text):
    intents = {
        "greeting": ["hello", "hi", "hey"],
        "weather_query": ["weather", "forecast", "temperature"],
        "location_query": ["location", "city", "town"],
        "faq": ["what", "how", "when"]
    }

    # Create a list of intent labels and corresponding texts
    intent_labels = []
    intent_texts = []
    for intent, keywords in intents.items():
        for keyword in keywords:
            intent_labels.append(intent)
            intent_texts.append(keyword)

    # Split the data into training and testing sets
    train_texts, test_texts, train_labels, test_labels = train_test_split(intent_texts, intent_labels, test_size=0.2, random_state=42)

    # Vectorize the text data
    vectorizer = TfidfVectorizer()
    train_vectors = vectorizer.fit_transform(train_texts)
    test_vectors = vectorizer.transform(test_texts)

    # Train a Naive Bayes classifier
    classifier = MultinomialNB()
    classifier.fit(train_vectors, train_labels)

    # Classify the input text
    input_vector = vectorizer.transform([input_text])
    prediction = classifier.predict(input_vector)

    return prediction[0]

# Test the function
input_text = "What's the weather like today?"
print(classify_intent(input_text))