from pdfminer.high_level import extract_text
import re
from tkinter_UI import SpeedReaderApp

books = "/Users/golden/Desktop/Books/Personal/"
grit = "Grit by Angela Duckworth.pdf"

text = extract_text(books + grit)
words = re.split("[ \n]+", text)

app = SpeedReaderApp(words, 0.10)
app.run()