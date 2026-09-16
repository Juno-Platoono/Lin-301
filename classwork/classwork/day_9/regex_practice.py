import re                                                     # loads Python's regex toolkit

with open("../../../data/gutenberg/alice.txt", encoding="utf-8") as f:  # opens alice.txt for reading
    text = f.read()                                           # reads the whole file into one string, called `text`

    matches = re.findall(r"c.t", text)   # finds every match of "c_t"
print(matches)                     # take a look at what it found
print(len(matches))                  # counts how many were found -- this matches grep -Eo's count
print(*matches, sep="\n")            # prints each match on a separate line

matches_aou = re.findall(r"c[aou]t", text)   # finds "cat", "cot", or "cut"
print(len(matches_aou))                      # counts how many were found
print(*matches_aou, sep="\n")                # prints each match on a separate line

matches_not_ao = re.findall(r"c[^ao]t", text)   # 
print(len(matches_not_ao))                      # 
print(*matches_not_ao, sep="\n")                # 

matches_a_q = re.findall(r"[a-q]t", text)   # 
print(len(matches_a_q))                      # 
print(*matches_a_q, sep="\n")                # 