import os
import re

HERE = os.path.dirname(__file__)   # the folder lin301.py lives in: data/

def ttr(words):
    t = len(set(words))/len(words)
    return t

def ttr_first(words, n=10000):
    return len(set(words[:n])) / len(words[:n])

def avg_word_len(words):
    wd_len_total = 0
    for w in words:
        wd_len_total += len(w)
    word_len = wd_len_total / len(words)
    return word_len


def load_words(filename):
    with open(os.path.join(HERE, "gutenberg", filename), "r", encoding="utf-8") as f:
        lines = f.readlines()

    while not lines[0].startswith("*** START"):
        lines = lines[1:]
    lines = lines[1:]

    while not lines[-1].startswith("*** END"):
        lines = lines[:-1]
    lines = lines[:-1]

    text = "".join(lines)
    words = re.split(r"[\W]+", text.lower())
    words = [w for w in words if w != ""]
    return words
#so now you would do alice_words = load_words("alice.txt")

def report(title, words):
    print(title, "TTR:", ttr(words))
    print(title, "TTR (10,000 words):", ttr_first(words))
    print(title, "Average Word Length:", avg_word_len(words))
    return ttr_first(words)
#eg ("alice in wonderland", alice_words) if alice_words is already def

#example of importing below

#import sys
#sys.path.append("../../../data")   # look for files in data/, too
#import lin301

#alice_words = lin301.load_words("alice.txt")
#lin301.ttr_first(alice_words)