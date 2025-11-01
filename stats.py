import pprint

def count_words(text):
    words = text.split()    
    num_words = len(words)
    return num_words

def char_count(text):
    dict = {}
    for w in text.lower():
        if w.isalpha():
            if w not in dict:
                dict[w] = 0
            dict[w] +=1
    return dict