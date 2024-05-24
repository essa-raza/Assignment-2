from __future__ import division
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn import metrics
from operator import itemgetter
from sklearn.metrics import classification_report
import csv, os, codecs, fnmatch
import numpy as np
from sklearn import metrics
from sklearn import svm
from sklearn import cross_validation
import pandas as pd

# Important libraries

usefulJSpaths = []  # absolute path of functional Javascript codes
usefulJSfiles = []  # list of file names
rusefulJSfiles = []  # list of opened files
n_features = 190

gmv = 0.001  # 0.001 # 0.05 # 0.1 # 0.5 # 0.1, 0.05, 0.01, 0.005, 0.001
nuv = 0.001  # 0.1, 0.05, 0.01, 0.005, 0.001

for root, dirnames, filenames, in os.walk('/Users/ikram/Desktop/GroundTruth-New/Data/GTPDG/Useful/'):
    for filename in fnmatch.filter(filenames, "*.js"):
        usefulJSfiles.append(filename)
        usefulJSpaths.append(os.path.join(root, filename))
        try:
            with codecs.open(os.path.join(root, filename)) as f:  # No need to specify 'r': this is the default.
                rusefulJSfiles.append(unicode(f.read(),
                                              errors='ignore'))  # inline Cosine similarity, Cosine does work on whole doc so no .split()
        except IOError as exc:
            if exc.errno != errno.EISDIR:  # Do not fail if a directory is found, just ignore it.
                raise  # Propagate other kinds of IOError.

uselessJSpaths = []  # absolute path of tracking Javascript codes
uselessJSfiles = []
ruselessJSfiles = []  # list of opened files

for ulessroot, ulessdirnames, ulessfilenames, in os.walk('/Users/ikram/Desktop/GroundTruth-New/Data/GTPDG/useless/'):
    for filename in fnmatch.filter(ulessfilenames, "*.js"):
        uselessJSfiles.append(filename)
        uselessJSpaths.append(os.path.join(ulessroot, filename))
        try:
            with codecs.open(os.path.join(ulessroot, filename)) as f:  # No need to specify 'r': this is the default.
                ruselessJSfiles.append(unicode(f.read(),
                                               errors='ignore'))  # inline Cosine similarity, Cosine does work on whole doc so no .split()
        except IOError as exc:
            if exc.errno != errno.EISDIR:  # Do not fail if a directory is found, just ignore it.
                raise  # Propagate other kinds of IOError.

print("Number of useless JS files: %s " % len(ruselessJSfiles))
print("Number of useful JS files: %s " % len(rusefulJSfiles))
print("useful JS vs useless JS (ratio) : %s " % (len(rusefulJSfiles) / len(ruselessJSfiles)))

################### Feature Extraction

# you code goes here

################## Training Phase

# your code goes here

################## Testing Phase
# your code goes here

################## Analysis Phase
# your code goes here



