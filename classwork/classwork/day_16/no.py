with open("../../../data/gutenberg/mansfield_park.txt", "r", encoding="utf-8") as f:
    book_text = f.read()

with open("../../data/gutenberg/mansfield_park.txt", "r", encoding="utf-8") as f:
    book_lines = f.readlines()

#one_line = book_lines[139]
#one_line.rstrip() #l.strip, .strip
#one_line.strip().lower()
for line in book_lines[100:105]:
    print(line.strip().lower())

print(len(book_lines))

print(book_text[:200])