#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import codecs
import distance
from scipy.cluster.hierarchy import linkage, dendrogram
from matplotlib import pyplot as plt

class Sensim:
    def __init__(self, datafile):
        try:
            f = codecs.open(datafile, "r", "utf-8")
        except OSError:
            print('Cannot open', datafile)
            return

        self.ids = []
        self.data_list = []

        self._f2l(f)

        self.data_size = len(self.data_list)

    def _f2l(self, f):
        for line in f:
            id, data = line.rstrip('\n\r').split(',', 1)
            self.ids.append(id)
            self.data_list.append(data)