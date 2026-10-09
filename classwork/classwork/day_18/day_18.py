import re
import matplotlib

try:
    with open("../../../data/gutenberg/alice.txt", "r", encoding="utf-8") as f:
        alice_text = f.read()
except FileNotFoundError:
    print("Couldn't find that file — check the filename and location.")

alice_list = re.split(r"[\W]+", alice_text)
alice_list = [w for w in alice_list if w != ""]
print(alice_list[0:100]) 

counts= {}
for w in counts:
    counts [w] += 1
else:
    counts [w] = 1
