# -*- coding: utf-8 -*-


import glob
import sys
import codecs
from pylab import *

val = []
names = []
for i in glob.glob("tuit*csv"):
    f = codecs.open(i, "r", "utf-8")
    data = f.readlines()
    f.close()

    name = i.strip()
    name = i.replace("tuits_", "")
    name = name.replace(".csv", "")

    val.append(len(data))
    names.append(name)

pos = arange(len(names))+.5

figure(1, figsize=(12,9))
barh(pos,val, align="center", color="#2ca25f")
yticks(pos, (names), fontsize="15")
grid(True)
title(u'Tuits emitidos por tus congresistas', fontsize="20")
xlabel(u'Número de tuits georeferenciados', fontsize="20")
tight_layout()
savefig("ranking_congresista.png")
