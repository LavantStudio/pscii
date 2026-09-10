import os, random

words = open("words.txt", "r").read().splitlines()

random.shuffle(words)
print(" ".join(words))
