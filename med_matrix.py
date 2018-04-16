# -*- coding: utf-8 -*-
"""
Created on Sat Apr 14 10:10:32 2018

@author: allen
"""
import numpy as np

count = 0;
vertices = 5;
dualVertices = 2;
edges = np.array([[0, 1], [1, 2], [2,3], [3,4], [4,0]]);
dualEdges = np.array([[5, 6],[5,6],[5,6], [5,6], [5,6]]);


dist = np.zeros(np.maximum(vertices, dualVertices));
B = np.zeros(len(edges));
outcome = 0;
for j  in range(0, 2**len(B)):
	B = np.zeros(len(edges));
	for k in range(0, len(np.fromstring(' '.join(np.binary_repr(j)), dtype=int, sep=' '))):
		B[k] = np.fromstring(' '.join(np.binary_repr(j)), dtype=int, sep=' ')[k];
	A = np.identity(vertices + dualVertices);
	for i in range(0, len(edges)):
		if(B[i] == 1): 
			A[edges[i,0], edges[i,1]] = A[edges[i,0], edges[i,1]] + 1;  
		else:
			A[dualEdges[i,0], dualEdges[i,1]] = A[dualEdges[i,0], dualEdges[i,1]] + 1;
			
		A[edges[i,1], edges[i,0]] = A[edges[i,0], edges[i,1]];
		A[dualEdges[i,1], dualEdges[i,0]] = A[dualEdges[i,0], dualEdges[i,1]];
	APower = np.heaviside(np.linalg.matrix_power(A, vertices),0);
	outcome = np.linalg.matrix_rank(APower) - 1;
	if(outcome > len(dist)): 
		np.concatenate(dist, [0],axis=0)
	for i in range(1,len(dist)+1):
		if(outcome == i):
			dist[i-1] = dist[i-1] + 1;
print(dist)