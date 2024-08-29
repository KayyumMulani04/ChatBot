import random
import json
import pickle
import numpy as np
import nltk
from nltk.stem import WordNetLemmatizer

from tensorflow import keras
from keras.models import Sequential
from keras.layers import Dense, Dropout
from keras import optimizers
from keras.models import load_model

import tkinter as tk

# Download NLTK resources
nltk.download('punkt')
nltk.download('wordnet')

# Load intents data
intents = json.loads(open('C:/Users/kayyum/python/AI chatbot/intents.json').read())

# Load lemmatizer
lemmatizer = WordNetLemmatizer()

# Load words and classes
words = pickle.load(open('C:/Users/kayyum/python/AI chatbot/words.pkl', 'rb'))
classes = pickle.load(open('C:/Users/kayyum/python/AI chatbot/classes.pkl', 'rb'))

# Load pre-trained model
model = load_model('C:/Users/kayyum/python/AI chatbot/chatbotmodel.h5')

def clean_up_sentence(sentence):
    sentence_words = nltk.word_tokenize(sentence)
    sentence_words = [lemmatizer.lemmatize(word.lower()) for word in sentence_words]
    return sentence_words

def bag_of_words(sentence):
    sentence_words = clean_up_sentence(sentence)
    bag = [0]*len(words)
    for w in sentence_words:
        for i, word in enumerate(words):
            if word == w:
                bag[i] = 1
    return np.array(bag)

def predict_class(sentence):
    bow = bag_of_words(sentence)
    res = model.predict(np.array([bow]))[0]
    ERROR_THRESHOLD = 0.25
    results = [[i, r] for i, r in enumerate(res) if r > ERROR_THRESHOLD]

    results.sort(key=lambda x: x[1], reverse=True)
    return_list = []
    for r in results:
        return_list.append({'intent': classes[r[0]], 'probability': str(r[1])})
    return return_list

def get_response(intents_list, intents_json):
    tag = intents_list[0]['intent']
    list_of_intents = intents_json['intents']
    for i in list_of_intents:
        if i['tag'] == tag:
            result = random.choice(i['responses'])
            break
    return result


def send_message(event=None):
    message = entry_field.get()
    if message.strip() == "":
        return

    entry_field.delete(0, tk.END)

    ints = predict_class(message)
    res = get_response(ints, intents)

    chat_history.config(state=tk.NORMAL)
    chat_history.insert(tk.END, "You: " + message + "\n")
    chat_history.insert(tk.END, "Bot: " + res + "\n\n")
    chat_history.config(state=tk.DISABLED)

root = tk.Tk()
root.title("Chatbot")

chat_history = tk.Text(root, bd=1, bg="white", height="10", width="60", font="Arial", padx=10, pady=10)
chat_history.config(state=tk.DISABLED)
scrollbar = tk.Scrollbar(root, command=chat_history.yview, cursor="heart")
chat_history['yscrollcommand'] = scrollbar.set

entry_field = tk.Entry(root, bg="white", width="29", font="Arial")
entry_field.bind("<Return>", send_message)

send_button = tk.Button(root, text="Send", command=send_message)

# Use grid manager to place components
chat_history.grid(row=0, column=0, columnspan=2, sticky="nsew")
scrollbar.grid(row=0, column=2, sticky="ns")
entry_field.grid(row=1, column=0, columnspan=1, padx=6, pady=6, sticky="ew")
send_button.grid(row=1, column=1, padx=6, pady=6, sticky="ew")

# Configure resizing behavior
root.columnconfigure(0, weight=1)  # Allow column 0 to expand horizontally
root.rowconfigure(0, weight=1)      # Allow row 0 to expand vertically

root.mainloop()
