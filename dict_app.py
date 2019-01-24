import json
import difflib
from difflib import SequenceMatcher, get_close_matches

### Returns a key value pair of input word (or it's closest match) and it's definition ###
def define(word):
    if word in data:
        return {word: data[word]}

    else:
        # Declaring outside of for loop for comparison
        best_word = None
        best_ratio = 0

        # For loop through [WORD, word and Word] to check highest similarity ratio
        for x in [word.upper(), word.lower(), word.title()]:

            # get_close_matches with n = 1 will return list of len 1, containing only closest match found (if ratio > 0.6)
            match = get_close_matches(x, data.keys(), n = 1, cutoff = 0.6)

            # if no matches found for this VaRiAtIoN, continue
            if len(match) == 0:
                continue
            
            # similarity ratio of this iteration
            x_ratio = SequenceMatcher(None, match[0], x).ratio()

            # if this word's ratio is GT previous best, store this word as best_word, then it's ratio as best_ratio
            if x_ratio > best_ratio:
                best_word = match[0]
                best_ratio = x_ratio
                
        if best_ratio == 0:
            # if no matches found, return None value
            return None

        else:
            # otherwise return dict of {KEY = word and VAL(s) = definition(s)}
            return {best_word: data[best_word]}


# Start of program
data = json.load(open("data.json"))
word = input("Enter word: ")

# wd (word - definition) 
definition = define(word)

if definition == None:
    print("%s not found." %word)

word = list(definition.keys())[0]
definitions = list(definition.values())

print(" \t->%s" %word)
for e, i in enumerate(definitions[0]):
    print('%s\t%s' %(e+1, i))