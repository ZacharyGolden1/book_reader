from pdfminer.high_level import extract_text
import time

books = "/Users/golden/Desktop/Books/Personal/"
grit = "Grit by Angela Duckworth.pdf"

text = extract_text(books + grit)
words = text.split(" ")

for word in words:
    print(word)
    time.sleep(0.1)