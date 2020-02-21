# Easy word generating for hw2 
# Feb 21 2020
# Created by Matt Perry
import random

writeFile = "words.txt"
count = 1000*1000
wordfile = "/usr/share/dict/words"

words = open(wordfile).read().splitlines()
lenDict = len(words)
allWords = []
for size in range(count):
    allWords.append(words[random.randint(0,lenDict-1)])
sortedWords = sorted(allWords,key=str.lower)
with open(writeFile, "w") as file:
    for word in sortedWords:
        file.write("%s\n" %word)
