#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from sensim.sensim import Sensim
from matplotlib import pyplot as plt
from scipy.cluster.hierarchy import dendrogram

sensim = Sensim(sys.argv[1])
ids = sensim.get_ids()
result = sensim.ward()
mod_ids = [id[-6:] for id in ids]
r = dendrogram(result, p=100, truncate_mode='lastp', labels=mod_ids, leaf_rotation=90)
print(r['leaves'])
print(r['ivl'])
plt.ylim(ymin=-10.0)
plt.show()