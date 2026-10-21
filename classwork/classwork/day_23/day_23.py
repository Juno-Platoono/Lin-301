lang_info = {
    "Latin":    {"family": "Indo-European", "location": "Italy"},
    "Greek":    {"family": "Indo-European", "location": "Greece"},
    "Sanskrit": {"family": "Indo-European", "location": "India"},
    "Finnish":  {"family": "Uralic",        "location": "Finland"}
}

print("sanskrit family:",lang_info["Sanskrit"]["family"])

for lang, features in lang_info.items():
    if features["family"] == "Indo-European":
        print(lang,features["location"])

lexicon = {
    "bank": {"pos": "noun", "gloss": "edge of a river"},
    "bank": {"pos": "noun", "gloss": "place to keep money"}
}
print("lexicon:",lexicon)

lexicon = [
    {"form": "bank", "pos": "noun", "gloss": "edge of a river"},
    {"form": "bank", "pos": "noun", "gloss": "place to keep money"},
    {"form": "bank", "pos": "verb", "gloss": "to tilt an airplane"}
]
print("better lexicon:", lexicon)
print(lexicon[2]["gloss"]) # to tilt an airplane

for entry in lexicon:
    print(entry["form"], "(" + entry["pos"] + "):", entry["gloss"])

lang_rows = []

for lang, info in lang_info.items():
    lang_rows.append({
        "language": lang,
        "family": info["family"],
        "location": info["location"]
    })

print(lang_rows)

import pandas as pd

lang_df = pd.DataFrame(lang_rows)
print(lang_df)

fresh_df = pd.DataFrame({
    "language": ["Latin", "Greek", "Sanskrit", "Finnish"],
    "family":   ["Indo-European", "Indo-European", "Indo-European", "Uralic"],
    "location": ["Italy", "Greece", "India", "Finland"]
})

print(fresh_df)

#missing a row \/
rows = [
    {"form": "aqua", "gloss": "water"},
    {"form": "canis", "gloss": "dog", "pos": "noun"}
]

print(pd.DataFrame(rows))
#missing a row /\

consonant =  ["p", "b", "t", "d", "k", "g", "s", "z", "m", "n", "l", "r", "w", "j", "h"]
place = ["bilabial", "bilabial", "alveolar", "alveolar", "velar", "velar", "alveolar", "alveolar", "bilabial", "alveolar", "alveolar", "alveolar", "labial-velar", "palatal", "glottal"]
manner = ["stop", "stop", "stop", "stop", "stop", "stop", "fricative", "fricative", "nasal", "nasal", "lateral", "trill", "glide", "glide", "fricative"]
voice = ["voiceless", "voiced", "voiceless", "voiced", "voiceless", "voiced", "voiceless", "voiced", "voiced", "voiced", "voiced", "voiced", "voiced", "voiced", "voiceless"]




cons_df = pd.DataFrame({
        "consonant": consonant,
        "place": place,
        "manner": manner,
        "voice": voice
    })

print(cons_df)

#shit i dont get\/
lang_df.to_csv("languages.csv", index=False, encoding="utf-8-sig")
check = pd.read_csv("languages.csv")
print(check)
with open("../../../data/gutenberg/alice.txt", "r", encoding="utf-8") as f:
    raw_text = f.read()
    import re

words = re.split(r"[\W]+", raw_text.lower())
words = [w for w in words if w != ""]

rows = []
for w in words:
    rows.append({"word": w, "length": len(w)})
    import pandas as pd

words_df = pd.DataFrame(rows)
words_df.to_csv("words.csv", index=False, encoding="utf-8-sig")
check = pd.read_csv("words.csv")
print(len(words_df), len(check))
#/\ shit i dont get /\


forms     = ["aqua", "rosa", "amō", "canis", "magnus", "videō", "puella", "bonus", "dominus", "portō", "lupus", "longus"]
glosses   = ["water", "rose", "I love", "dog", "big", "I see", "girl", "good", "lord", "I carry", "wolf", "long"]
pos       = ["noun", "noun", "verb", "noun", "adj", "verb", "noun", "adj", "noun", "verb", "noun", "adj"]
syllables = [2, 2, 2, 2, 2, 3, 3, 2, 3, 2, 2, 2]

latin = {}

for f, g, p, s in zip(forms,glosses, pos, syllables):
    latin[f] = {"glosses": g, "pos": p, "syllables": s}

latin_rows = []

for form, info in latin.items():
    latin_rows.append({
        "forms": form,
        "glosses": info["glosses"],
        "pos": info["pos"],
        "syllables": info["syllables"]
    })
latin_df = pd.DataFrame(latin_rows)
print(latin_df)

latin_df.to_csv("latin.csv", index=False, encoding="utf-8-sig")