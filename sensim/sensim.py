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