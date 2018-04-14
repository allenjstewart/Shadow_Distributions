# -*- coding: utf-8 -*-
"""
Created on Sat Apr 14 10:10:32 2018

@author: allen
"""
import numpy as np

iniDist = np.array([3,4,1])
nCrossings = 1
nKnots = 5
prevKnots = iniDist
bigKnots = iniDist

for a in range(0, nKnots):
    if a > 1:
        prevKnots = bigKnots
        
    bigKnots = np.concatenate((np.zeros(len(prevKnots)),np.zeros(len(iniDist))),axis=0)
    for k in range(0,nKnots*len(iniDist)):
        for n in range(0,len(prevKnots)):
            for m in range(0,len(iniDist)):
                if n + m == k:
                    bigKnots[k] = bigKnots[k] + prevKnots[n]*iniDist[m]

print('Distribution for %.f knots\n',nKnots)
print(bigKnots)
