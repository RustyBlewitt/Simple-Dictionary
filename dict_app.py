import json

data = json.load(open("data.json"))

def translate(word):
    if word in data:
        return data[word]
    else:
        return "Word not found, please try again."

word = input("Enter word: ")

print(translate(word))