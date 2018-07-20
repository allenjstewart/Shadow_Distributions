# -*- coding: utf-8 -*-
"""
Created on Sat Apr 14 10:10:32 2018

@author: allen
"""
import numpy as np

#initialize the graph
count = 0
vertices = 5
dualVertices = 2
#It is important that the numbering of the edges and dual edges is increasing
#With respect to the first coordinate
edges = np.array([[0, 1], [1, 2], [2,3], [3,4], [4,0]])
dualEdges = np.array([[5, 6],[5,6],[5,6], [5,6], [5,6]])


dist = np.zeros(np.maximum(vertices, dualVertices)) #Vector of zeros whose size depends on whether the graph or dual has more vertices
B = np.zeros(len(edges)) #Vector of zeros whose size depends on the number of edges in the graph
outcome = 0 #Initialize the number of components after smoothing to zero

#The total number of ways to smooth the graph is 2^(number of edges) 
#Since each edge in the graph goes through a crossing
for j  in range(0, 2**len(B)): 
	B = np.zeros(len(edges)) #Reset B to be all zeros
	#The loop below will populate a vector B with the binary representation of the number j
	#binary_repr returns the binary representation of j as a strings
	#join concatenates all of the strings
	#fromstring creates a vector from the string
	for k in range(0, len(np.fromstring(' '.join(np.binary_repr(j)), dtype=int, sep=' '))):
		#Each entry of the vector B is now a binary digit of the number j
		B[k] = np.fromstring(' '.join(np.binary_repr(j)), dtype=int, sep=' ')[k] 
	#Create a block indentity matrix that will eventually be the adjaceny
	#Matrices of ther graph and its dual	
	A = np.identity(vertices + dualVertices) 
	for i in range(0, len(edges)):
		#If the ith binary digit of j is 1, then put a 1 in the adjacency matrix
		if(B[i] == 1): 
			A[edges[i,0], edges[i,1]] = A[edges[i,0], edges[i,1]] + 1
		#otherwise put a 1 in the dual adjacency matrix	
		else:
			A[dualEdges[i,0], dualEdges[i,1]] = A[dualEdges[i,0], dualEdges[i,1]] + 1
		#Populate the lower triangle of the graph adjacency matrix to make sure the matrix is symmetric	
		A[edges[i,1], edges[i,0]] = A[edges[i,0], edges[i,1]]
		#Do the same with the dual adjacency matrix
		A[dualEdges[i,1], dualEdges[i,0]] = A[dualEdges[i,0], dualEdges[i,1]]
	#At this point we have smoothed all of the crossings
	#And our matrix is the adjacency matrix of the graph at the end of the process
	#So our graph and its dual have some number of connected components
	#Take this matrix to a power to find the number of conented components
	#The heaviside function makes sure the matrix is just 1s and 0s     	
	APower = np.heaviside(np.linalg.matrix_power(A, vertices),0)
	#The rank of this matrix is the number of connected components
	outcome = np.linalg.matrix_rank(APower) - 1
	#Now that we know the number of connected components we check and see
	#If this is a new number of components or not
	if(outcome > len(dist)): 
		#If this is a new number of connected components, add a position to the distribution
		np.concatenate(dist, [0],axis=0)	
	for i in range(1,len(dist)+1):
		#Go through the distribution and
		#Add 1 to the value in the distribution associated to the number of components
		if(outcome == i):
			dist[i-1] = dist[i-1] + 1		
print(dist)