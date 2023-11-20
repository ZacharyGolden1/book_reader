from pdfminer.high_level import extract_text
import re
from tkinter_UI import SpeedReaderApp

books = "/Users/golden/Desktop/Books/Personal/"
grit = "Grit by Angela Duckworth.pdf"
hgtg = "THE_HITCHHIKERS_GUIDE_TO_THE_GALAXY 2.pdf"

text = extract_text(books + hgtg)
words = re.split("[ \n]+", text)

                            
app = SpeedReaderApp(words, 0.10, # delay (how many fractions of a second between words)
                    0)# what word to start on
app.run() 