import json
import difflib
from difflib import SequenceMatcher, get_close_matches

### Returns a key value pair of input word (or it's closest match) and it's definition ###
def translate(word):
    if word in data:
        return {word: data[word]}

    else:
        # get_close_matches with n = 1 will return list of size 1, containing closest matches of min 0.6 similarity ratio
        match = get_close_matches(word, data.keys(), n = 1, cutoff = 0.6)

        if len(match) == 0:
            return {word: "Word not found"}
        else:
            # {Best match found: Dict lookup for best match found}
            return {match[0]: data[match[0]]}


data = json.load(open("data.json"))
word = input("Enter word: ").lower()


wd = translate(word)
word = list(wd.keys())
definitions = list(wd.values())

print(" \t->%s" %word[0])

for e, i in enumerate(definitions[0]):
    print('%s\t%s' %(e+1, i))