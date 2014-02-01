# -*- coding: utf-8 -*-


import codecs
import prettyplotlib as ppl
import numpy as np
from prettyplotlib import plt
import csv


x = []
y = []
with open("congresistas.txt", "rb") as csvfile:
    f = csv.reader(csvfile, delimiter=",")
    for row in f:
        x.append(row[1].decode("utf-8"))
        y.append(row[0])

y = map(int, y)

plt.rc('font', **{'family': 'DejaVu Sans'})
fig, ax = plt.subplots(1, figsize=(20,16))

width = 0.35
ind = np.arange(len(y))
xdata = ind + 0.05 + width
ax.bar(ind, y)
ax.set_xticks(ind + 0.5)
ax.set_xticklabels(x, rotation="vertical")
ax.autoscale()
ax.set_title(u'Ranking de congresistas',
        fontdict = {'fontsize':36}
        )

plt.ylabel(u'Número de saludos oficiales', fontdict={'fontsize':32})
plt.xlabel(u'Congresista', fontdict={'fontsize':32})
plt.tick_params(axis="y", which="major", labelsize=24)

ppl.bar(ax, np.arange(len(y)), y, grid="y")
plt.tight_layout()
fig.savefig("ranking_congresista.png")
