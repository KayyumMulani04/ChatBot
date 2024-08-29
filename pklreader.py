import pickle

# Load the pickle file
with open('C:/Users/kayyum/python/AI chatbot/words.pkl', 'rb') as w:
     data1 = pickle.load(w)

# Print the contents
print(data1)

with open('C:/Users/kayyum/python/AI chatbot/classes.pkl', 'rb') as f:
    data = pickle.load(f)

 #Print the contents
print(data)
