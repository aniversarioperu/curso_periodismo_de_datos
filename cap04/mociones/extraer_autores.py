#!/usr/bin/env python

# -*- coding: utf-8 -*-  

import glob
from bs4 import BeautifulSoup
import codecs


for i in glob.glob('*html'):
    f = codecs.open(i, "r", "latin1")
    html = f.read()
    f.close()

    soup = BeautifulSoup(html)
    for td in soup.find_all('td', 'menu1', valign='top', width='150'):
        authores = td.get_text()
        authores = authores.split("\n")
        for i in authores:
        print authores
