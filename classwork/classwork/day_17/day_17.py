#words = ["phoneme", "phrase", "morpheme", "reconstruction", "index"]

#clean = [term.strip().lower() for term in words]
#shouting =[term.strip().upper() for term in words]
#lengths =[len(term) for term in words]
#firsts = [term[0] for term in words]


try:
    with open("../../../data/gutenberg/mansfield_park.txt", "r", encoding="utf-8") as f:
        book_lines = f.readlines()
except FileNotFoundError:
    print("Couldn't find that file — check the filename and location.")

mansfield_cleaned = [line.strip().lower() for line in book_lines]
mansfield_nonempty = [line for line in mansfield_cleaned if line != ""]

print(book_lines[100:105])
print(mansfield_cleaned[100:105])


items = ["color", "flavour", "theater", "center", "analyze", "organize", "favorite", "neighbor", "honor", "catalog", "honour", "flavor", "analyse", "flavor", "traveler"]

r_item_count = 0
for item in items:
    if item[-1] == "r":
        r_item_count += 1
        print(item, r_item_count)

c_item_count = 0
for item in items:
    if item[0] == "c":
        c_item_count += 1
        print(item, c_item_count)