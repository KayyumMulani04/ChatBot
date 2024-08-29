import pickle

# Load existing words from the pickle file
existing_words = ["'s", 'Awesome', 'BBA', 'BIT', 'Day', 'Good', 'Goodbye', 'Greetings', 'Have', 'I', 'Is', 'See', 'Thank', 'Thanks', 'That', 'What', 'a', 'activity', 'admission', 'am', 'any', 'are', 'asbhk', 'available', 'be', 'by', 'bye', 'call', 'class', 'college', 'complete', 'conduct', 'course', 'curriculum', 'cya', 'day', 'different', 'doe', 'entry', 'exam', 'extra', 'facility', 'fee', 'for', 'format', 'from', 'fun', 'going', 'good', 'guy', 'gvsd', 'hello', 'helpful', 'helping', 'hey', 'hi', 'hour', 'how', 'in', 'infrastructure', 'is', 'it', 'later', 'leaving', 'like', 'located', 'location', 'long', 'many', 'me', 'month', 'much', 'name', 'of', 'one', 'open', 'operation', 'or', 'other', 'pattern', 'program', 'provided', 'requirement', 'see', 'semester', 'should', 'single', 'structure', 'student', 'study', 'style', 'take', 'teaching', 'thanks', 'the', 'there', 'this', 'to', 'up', 'what', 'when', 'where', 'who', 'will', 'ya', 'year', 'you', 'your', 'admissiondeadlines', 'contactdetails']
try:
    with open('C:/Users/kayyum/python/AI chatbot/words.pkl', 'rb') as f:
        existing_words = pickle.load(f)
except FileNotFoundError:
    print("File not found or empty. Creating a new one.")

# Words to remove
words_to_remove = ['admissiondeadlines', 'contactdetails']

# Remove words from the existing list
existing_words = [word for word in existing_words if word not in words_to_remove]

# Save the updated list back to the pickle file
with open('C:/Users/kayyum/python/AI chatbot/words.pkl', 'wb') as f:
    pickle.dump(existing_words, f)

print("Words removed from words.pkl")
