import os, random

words=open("words.txt","r").read().splitlines()
print(random.choice(words))
