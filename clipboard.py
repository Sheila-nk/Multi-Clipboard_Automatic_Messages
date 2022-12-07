import sys, pyperclip

#declare a dictionary of messages we would like to copy to clipboard
messages = {
    "response": "I appreciate your swift response!\nI will work on the recommended changes.",
    "unsure": "I am unaware of the intricacies of this situation.\nI will get back to you on it after some research.",
    "feeback": "I appreciate your feedback.\n I will implement the recommended changes.",
    "resources": "Thank you for the resources.\n I will be sure to check them out.",
    "review": "I would like you to review my pull request.\n I have provided the link below.",
    "merge": "Thank you for reviewing and merging my pull request.",
    "agree": "Yes, I agree. That sounds fine to me."
}

#check that user provides two arguments
if len(sys.argv) != 2:
    print("Usage: python clipboard.py <phrase>")
    sys.exit()

#second argument is the phrase whose value to copy
phrase = sys.argv[1]

#check if phrase is in our dictionary
if phrase not in messages:
    print("Phrase not found. Would you like to update the database with this phrase?")
    response = input("Type y for yes and n for no: ").lower()
    if response != 'y':
        sys.exit()
    print("What is the message associated with this phrase?")
    answer = input()
    messages[phrase] = answer
    print("Database updated!")

#get the selected message and copy it to the clipboard
message = messages[phrase]
pyperclip.copy(message)
print("Message for phrase '{}' copied to clipboard".format(phrase))