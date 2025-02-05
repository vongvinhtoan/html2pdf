# import html parser
from bs4 import BeautifulSoup
import pdfkit

# Read the file
with open("problem_ru.html", "r", encoding="utf-8") as file:
    html = file.read()

# Read the header
with open("header.html", "r", encoding="utf-8") as file:
    header = file.read()

# parse the html
header = BeautifulSoup(header, "html.parser")

# insert html to header body
header.body.insert(0, BeautifulSoup(html, "html.parser"))

html = header.prettify()

# from string
pdfkit.from_string(html, "index.pdf", verbose=True, options={"enable-local-file-access": True})
print("="*50)