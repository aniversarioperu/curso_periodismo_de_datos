# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import codecs
import glob

apellido = u"Julca"

for filename in glob.glob("*html"):
    f = codecs.open(filename, "r", "latin1")
    html_doc = f.read()
    f.close()
    soup = BeautifulSoup(html_doc)
    for tag in soup.find_all("td", width="150"):
        if apellido.lower() in tag.text.lower():
            prev = tag.previous_element
            prev2 = prev.previous_element
            prev3 = prev2.previous_element
            print prev3.previous_element.encode("utf8")
