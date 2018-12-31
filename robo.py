import nltk
import numpy as np
import random
import string # to process standard python strings
from sklearn.feature_extraction.text import TfidfVectorizer  
from sklearn.metrics.pairwise import cosine_similarity

f = open('chatbot.txt','r',errors='ignore')
raw = f.read()
raw = raw.lower()

nltk.download('punkt') 
nltk.download('wordnet')

sent_tokens = nltk.sent_tokenize(raw) # converts to a list of sentences
word_tokens = nltk.word_tokenize(raw) # converts ot a list of words

lemmer = nltk.stem.WordNetLemmatizer()
# WordNet is a semantically-oriented dictionary of English included in NLTK.

remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)

def LemTokens(tokens):
    """Returns a list of lemmatized tokens using the WordNet dictionary."""
    return [lemmer.lemmatize(token) for token in tokens]

def LemNormalize(text):
    return LemTokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))


GREETING_INPUTS = ("hello", "hi", "greetings", "sup", "what's up", "hey",)
GREETING_RESPONSES = ["hi", "hey", "*nods", "hi there", "hello", "I am glad! You are talking to me"]

def greeting(sentence):
    """The Robot greets us using a random greeting"""

    for word in sentence.split():
        if word.lower() in GREETING_INPUTS:
            return random.choice(GREETING_RESPONSES)


def response(user_response):
    robo_response = ''
    sent_tokens.append(user_response)
    TfidfVec = TfidfVectorizer(tokenizer=LemNormalize, stop_words='english')
    tfidf = TfidfVec.fit_transform(sent_tokens)
    vals = cosine_similarity(tfidf[-1], tfidf)
    idx = vals.argsort()[0][-2]
    flat = vals.flatten()
    flat.sort()
    req_tfidf = flat[-2]

    if(req_tfidf==0):
        robo_response=robo_response+"I am sorry! I don't understand you."
        return robo_response
    else:
        robo_response = robo_response+sent_tokens[idx]
        return robo_response
flag = True
print("Robo: My name is Robo. I will answer our queries about Chatbots. If you want ot exit, type  Bye!")

while(flag==True):
    user_response = input()
    user_response = user_response.lower()
    if(user_response !='bye'):
        if (user_response=='thanks' or user_response=='thank you'):
            flag=False
            print("Robo: You are welcome.")
        else:
            if (greeting(user_response)!= None):
                print("Robo: " + greeting(user_response))
            else:
                print("Robo: ", end="")
                print(response(user_response))
                sent_tokens.remove(user_response)
    else:
        flag=False
        print("Robo: Bye! Take care.")
