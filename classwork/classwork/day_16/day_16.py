word = input("Give me an English noun, in the singular: ")

sibilants = ["s", "z", "ʃ", "ʒ", "tʃ", "dʒ"] 
voiceless = ["p", "t", "k", "f", "θ"]

if word[-1] in sibilants:
    plural = word + "Iz"

elif word[-1] in voiceless:
    plural = word + "s"
else:
    plural = word + "z"

print(plural)

words = ["phoneme", "phrase", "morpheme", "reconstruction", "index"]
for title in words:
    print("the word",title,"has",len(title),"letters.")