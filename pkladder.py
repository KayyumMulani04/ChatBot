import pickle

# Load existing words from the pickle file
existing_classes = ['Location', 'classes', 'courseDuration', 'courses', 'exams', 'facilities', 'fee', 'funActivities', 'goodbye', 'greetings', 'hours', 'invalid', 'name', 'semDuration', 'semesters', 'studentRequirements', 'teachingStyle', 'thanks']
try:
    with open('C:/Users/kayyum/python/AI chatbot/classes.pkl', 'rb') as f:
        existing_classes = pickle.load(f)
except FileNotFoundError:
    print("File not found or empty. Creating a new one.")

# New words to insert
new_classes = ['semester','semDuration']

# Append new words to the existing list
existing_classes.extend(new_classes)

# Save the updated list back to the pickle file
with open('C:/Users/kayyum/python/AI chatbot/classes.pkl', 'wb') as f:
    pickle.dump(existing_classes, f)

print("New words inserted into classes.pkl")
