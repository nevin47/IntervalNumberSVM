__author__ = 'nevin47'

from numpy import *
import SVM
import matplotlib.pyplot as plt
import IntervalNum
if not "/IntervalNumCore" in sys.path:
    sys.path.append("/IntervalNumCore")
import HyperIntervalNumber