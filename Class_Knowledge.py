import random
from urllib.request import urlopen

"""The purpose of this program is to test the user's knowledge on objects and classes using generated prompts and randomized elements for 
repeated use."""

WORD_URL = "http://learncodethehardway.org/words.txt"
WORDS = []

#A dictionary where the keys represent lines of code and the values explain the code in ordinary english.
#%%% represents class names, @@@ represents multiple parameters, *** represents objects, functions, and/or values.
PHRASES = {"class %%%(%%%):":"%%% is a class that inherits from the %%% class.", 
           "class %%%():\n\t def __init__(self, ***)" : "class %%% has an __init__ function that takes self and *** parameters.",
           "class %%%():\n\t def ***(self, @@@)":"The class %%% has a function *** that takes self and @@@ parameters.",
           "*** = %%%()": "*** is set to an instance of the %%% class.",
           "***.***(@@@)":"Using the *** object call the *** function with the params: self, @@@.",
           "***.*** = '***'":"Using the *** object assign the *** attribute to '***'."}

#Ask for the user's test preference
print("If you want to convert code to english, enter 1. If you want to convert english to code, enter 2.")
answer = input("> ")

if answer == '1':
    PHRASE_FIRST = True
else:
    PHRASE_FIRST = False

#load up the words from the website
for word in urlopen(WORD_URL).readlines():
    WORDS.append(str(word.strip(), encoding="utf-8"))

def convert(snippet, phrase):
    #Create a list of random words equivalent to the number of %%% in the snippet, then capitalize each word.
    class_names = [w.capitalize() for w in random.sample(WORDS, snippet.count("%%%"))]

    #Create a list of random words equivalent to the number of *** in the snippet.
    other_names = random.sample(WORDS, snippet.count("***"))

    results = []
    param_names =[]
    
    #If @@@ appears in the snippet, create a list of 1-3 random words, join them by commas, and append the joined result to the param_names list.
    for i in range(0, snippet.count("@@@")):
        param_count = random.randint(1,3)
        param_names.append(', '.join(random.sample(WORDS, param_count)))
    
    #Fill in the blanks with the proper collected words.
    for sentence in snippet, phrase:    
        
        #Set result equal to snippet, make replacements, then repeat by setting it equal to phrase. 
        result = sentence[:]
        
        #Replace %%% with class names
        for word in class_names:
            result = result.replace("%%%",word,1)

        #Replace *** with other names
        for word in other_names:
            result = result.replace("***", word,1)
        
        #Replace @@@ with the element in param_names
        for word in param_names:
            result = result.replace("@@@", word,1)
        
        results.append(result)
    
    return results

#keep going until they hit CTRL-Z
print("Enter Crtl-Z at any time to end testing.")
try:

    while True:
        
        snippets = list(PHRASES.keys())
        random.shuffle(snippets)
        
        for snippet in snippets:
            phrase = PHRASES[snippet]
            question, answer = convert(snippet,phrase)
            
            if PHRASE_FIRST:
                question, answer = answer, question
            
            print(question)
            
            input("> ")
            print(f"ANSWER: {answer}\n\n")

except EOFError:
    print("\nBye")