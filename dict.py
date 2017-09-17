import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(word) :
    word = word.lower()
    if word in data:
        return data[word]
    elif len(get_close_matches(word, data.keys(), cutoff = 0.7)) > 0:
        yn = input("Did you mean %s instead? Enter Y is yes, or N if no. " % get_close_matches(word, data.keys(), cutoff = 0.7)[0])
        if yn == "Y" or yn == "y":
            return data[get_close_matches(word, data.keys(), cutoff = 0.7)[0]]
        elif yn == "N" or yn == "n":
            return "The word does not exist."
        else:
            return "Please answer the question properly."
    else:
        return "The word does not exist."




word = input("Enter a word: ")
output = translate(word)
count = 1

if type(output) == list: #output printed is either a string or a list (check return values)
    for item in output:
        print(str(count) + ". " + item)
        count += 1
else:
    print(output)
