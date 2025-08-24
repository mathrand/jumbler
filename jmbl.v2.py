#!/usr/bin/env python
# math.rand@gmail.com
 
import datetime
import sys
 
chrz = [
    "a",
    "@",
    "a",
    "4",
    "e",
    "3",
    "i",
    "!",
    "i",
    "1",
    "o",
    "0",
    "s",
    "5",
    "s",
    "$",
    "t",
    "7",
]
 
 
def sub(letter):
    global chrz
    i = 0
    letterz = []
    while i < len(chrz):
        if letter == chrz[i]:
            letterz.append(chrz[i + 1])
        i += 2
    letterz.append(letter.lower())
    letterz.append(letter.upper())
    return letterz
 
 
def loopy(word, position_in_word, old_characters):
    word_length = len(word)
    for variation in sub(word[position_in_word]):
        if len(old_characters + variation) == len(word):
            print(old_characters + variation)
        if (word_length - 1) > position_in_word:
            loopy(word, position_in_word + 1, old_characters + variation)
 
 
def print_time_now(word):
    now = datetime.datetime.now()
    print(word + " " + now.strftime("%Y-%m-%d %H:%M:%S"), file=sys.stderr)
 
 
if __name__ == "__main__":
    try:
        w = sys.argv[1]
    except:
        print(
            "App to l337ify/capitilise and create every possible permutation possible with the substition dictionary"
        )
        sys.exit("usage: python jmbl.py <your word>")
 
    print_time_now("started")  # prints to stderr
    loopy(w, 0, "")
    print_time_now("finished")  # prints to stderr
