from collections import *
import re

with open("log.txt", "r") as file: # не знаходить log.txt :(
    text = file.read().lower()

words = re.findall(r'\b\w+\b', text)

counter = Counter(words)
top_10 = counter.most_common(10)

with open("word_stats.txt", "w") as file:
    for word, count in top_10:
        file.write(f"{word}: {count}\n")

print("Результати записано у word_stats.txt")