import nltk
import numpy as np
import random
import string

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
corpus = [
    "Hi",
    "Hello",
    "How are you?",
    "I am fine",
    "What is your name?",
    "My name is ChatBot",
    "What can you do?",
    "I can answer your questions",
    "Bye",
    "Goodbye"
]
lemmer = nltk.stem.WordNetLemmatizer()

def LemTokens(tokens):
    return [lemmer.lemmatize(token) for token in tokens]

def LemNormalize(text):
    return LemTokens(
        nltk.word_tokenize(text.lower().translate(
            str.maketrans('', '', string.punctuation)
        ))
    )

greeting_inputs = ("hello", "hi", "hey")
greeting_responses = ["Hi!", "Hello!", "Hey there!"]

def greeting(sentence):
    for word in sentence.split():
        if word.lower() in greeting_inputs:
            return random.choice(greeting_responses)
def response(user_input):
    corpus.append(user_input)

    vectorizer = TfidfVectorizer(tokenizer=LemNormalize, stop_words='english')
    tfidf = vectorizer.fit_transform(corpus)

    similarity = cosine_similarity(tfidf[-1], tfidf)
    idx = similarity.argsort()[0][-2]

    flat = similarity.flatten()
    flat.sort()
    score = flat[-2]

    if score == 0:
        reply = "Sorry, I didn't understand that."
    else:
        reply = corpus[idx]

    corpus.pop()
    return reply

# Chat loop
print("ChatBot: Hello! Ask me something. Type 'bye' to exit.")

while True:
    user_input = input("You: ").lower()

    if user_input == "bye":
        print("ChatBot: Goodbye! 👋")
        break
    elif greeting(user_input):
        print("ChatBot:", greeting(user_input))
    else:
        print("ChatBot:", response(user_input))
import nltk
import numpy as np
import random
import string
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
corpus = [
    "Hi",
    "Hello",
    "How are you?",
    "I am fine",
    "What is your name?",
    "My name is ChatBot",
    "What can you do?",
    "I can answer your questions",
    "Bye",
    "Goodbye"
]
lemmer = nltk.stem.WordNetLemmatizer()

def LemTokens(tokens):
    return [lemmer.lemmatize(token) for token in tokens]

def LemNormalize(text):
    return LemTokens(
        nltk.word_tokenize(text.lower().translate(
            str.maketrans('', '', string.punctuation)
        ))
    )
greeting_inputs = ("hello", "hi", "hey")
greeting_responses = ["Hi!", "Hello!", "Hey there!"]
def greeting(sentence):
    for word in sentence.split():
        if word.lower() in greeting_inputs:
            return random.choice(greeting_responses)
def response(user_input):
    corpus.append(user_input)
    vectorizer = TfidfVectorizer(tokenizer=LemNormalize, stop_words='english')
    tfidf = vectorizer.fit_transform(corpus)
    similarity = cosine_similarity(tfidf[-1], tfidf)
    idx = similarity.argsort()[0][-2]
    flat = similarity.flatten()
    flat.sort()
    score = flat[-2]
    if score == 0:
        reply = "Sorry, I didn't understand that."
    else:
        reply = corpus[idx]
    corpus.pop()
    return reply
print("ChatBot: Hello! Ask me something. Type 'bye' to exit.")

while True:
    user_input = input("You: ").lower()

    if user_input == "bye":
        print("ChatBot: Goodbye! 👋")
        break
    elif greeting(user_input):
        print("ChatBot:", greeting(user_input))
    else:
        print("ChatBot:", response(user_input))
