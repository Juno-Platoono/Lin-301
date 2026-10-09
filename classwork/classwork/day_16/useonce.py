import urllib.request

url = "https://www.gutenberg.org/cache/epub/1513/pg1513.txt"  # Mansfield Park
filename = "../../../data/gutenberg/rnj.txt"

try:
    urllib.request.urlretrieve(url, filename)
    print("Downloaded:", filename)
except FileNotFoundError:
    print("Couldn't save the file — does the ../../data/gutenberg/ folder exist?")