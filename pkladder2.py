import pickle

# Load existing words from the pickle file
existing_words = ["'s", 'Awesome', 'BBA', 'BIT', 'Day', 'Good', 'Goodbye', 'Greetings', 'Have', 'I', 'Is', 'See', 'Thank', 'Thanks', 'That', 'What', 'a', 'activity', 'admission', 'am', 'any', 'are', 'asbhk', 'available', 'be', 'by', 'bye', 'call', 'class', 'college', 'complete', 'conduct', 'course', 'curriculum', 'cya', 'day', 'different', 'doe', 'entry', 'exam', 'extra', 'facility', 'fee', 'for', 'format', 'from', 'fun', 'going', 'good', 'guy', 'gvsd', 'hello', 'helpful', 'helping', 'hey', 'hi', 'hour', 'how', 'in', 'infrastructure', 'is', 'it', 'later', 'leaving', 'like', 'located', 'location', 'long', 'many', 'me', 'month', 'much', 'name', 'of', 'one', 'open', 'operation', 'or', 'other', 'pattern', 'program', 'provided', 'requirement', 'see', 'semester', 'should', 'single', 'structure', 'student', 'study', 'style', 'take', 'teaching', 'thanks', 'the', 'there', 'this', 'to', 'up', 'what', 'when', 'where', 'who', 'will', 'ya', 'year', 'you', 'your']
try:
    with open('C:/Users/kayyum/python/AI chatbot/words.pkl', 'rb') as f:
        existing_words = pickle.load(f)
except FileNotFoundError:
    print("File not found or empty. Creating a new one.")

# New words to insert
new_words = ['admissiondeadlines','contactdetails']

# Append new words to the existing list
existing_words.extend(new_words)

# Save the updated list back to the pickle file
with open('C:/Users/kayyum/python/AI chatbot/words.pkl', 'wb') as f:
    pickle.dump(existing_words, f)

print("New words inserted into words.pkl")
