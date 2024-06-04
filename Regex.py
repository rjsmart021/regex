#1. Python Regular Expressions Mastery
#Task 1: Code Correction
import re
text = "Contact emails are: john.doe@example.com and jane.doe@example.com."
emails = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", text)
print(emails)
#2. Python Regular Expressions Deep Dive
#Task 1: Email Extraction Enhancement
import re

text = "Emails: user1@domain.com, user2@exclude.com, user3@domain.com"
emails = re.findall(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b", text)
print(emails)
filtered_emails = []
for email in emails:
    if not re.match("[A-Za-z0-9._%+-]+@exclude\.com", email):
        filtered_emails.append(email)
print(filtered_emails)
#3. Advanced Text Processing with Python Regex
#Task 1: Advanced Data Extraction
import re

text = "Name: John Doe; Age: 30; Occupation: Engineer; Location: New York"
# Extract the Occupation from the text
# Your code here
import re

text = "Name: John Doe; Age: 30; Occupation: Engineer; Location: New York"
key = "Occupation"
pattern = f"({key}): ([\sA-Za-z0-9._%+-]+);"
variable = re.search(pattern,text)
print(variable.group(2))
# Extract the Occupation from the text


# function take in argument that takes in the key 
descriptions = [
    "Smartphone with 6-inch screen and 128GB memory",
    "Cotton t-shirt in medium size",
    "Stainless steel kitchen knife set"
]

key_wordselectronic = ["smartphone", "screen", "memory", "gigabites"]
key_wordsclothing = ["t-shirt", "blouse", "yarn", "silk", "coat"]
key_wordskitchen = ["kitchen", "knife", "spoon", "fork"]
for product in descriptions:
    words = re.findall("\w+", product)
    for word in words:
        if word in key_wordselectronic:
            print("electronics")
        if word in key_wordsclothing:
            print("clothing")
        if word in key_wordskitchen:
            print("kitchen")
