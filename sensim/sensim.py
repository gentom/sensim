#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import codecs
from distance import levenshtein
from scipy.cluster.hierarchy import linkage, dendrogram

class Sensim:
    def __init__(self, datafile):
        try:
            f = codecs.open(datafile, "r", "utf-8")
        except OSError:
            print('Cannot open', datafile)
            return

        self.ids = []
        self.data_list = []
        self.data_size = 0
        self.distances = []

        self._f2l(f)

        self.data_size = len(self.data_list)

    def _f2l(self, f):
        for line in f:
            id, data = line.rstrip('\n\r').split(',', 1)
            self.ids.append(id)
            self.data_list.append(data)

    def distance(self):
        for i in range(self.data_size - 1):
            for j in range(i+1, self.data_size):
                similarity = levenshtein(self.data_list[i], self.data_list[j])
                self.distances.append(similarity)
    
    def ward(self):
        return linkage(self.distances, method='ward')