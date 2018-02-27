# -*- coding: utf-8 -*-
"""
Created on Mon Feb 26 18:10:18 2018

@author: lokesh.r
['A', 'C', 'A', 'D', 'G', 'I', 'L', 'D']
['x', 'y', 'z', 'xx', 'yy', 'zz', 'xx', 'yy', 'zz', 'xxxx', 'yyyy', 'zzzz']
[[2], [3], [4], [3], [4], [5], [4], [5], [6]]
[[2, 3, 4, 5], [3, 4, 5, 6], [4, 5, 6, 7], [5, 6, 7, 8]]
[(1, 1), (2, 1), (3, 1), (1, 2), (2, 2), (3, 2), (1, 3), (2, 3), (3, 3)]

"""

str = "ACADGILD"
Y = [i for i in str]
print(Y)


Y = [j*i for i in ['x','y','z'] for j in range(1,5)]
print(Y)

X= ['x','y','z']

Z = [i*a for a in  [1,2,2,4] for i in X ]
print(Z)


A = [[x+y] for x in [1,2,3]  for y in [1,2,3]]
print(A)

A = [[x,y+1,z+2,z1+3] for x in range(2,6)  for y in range(x,x+1) for z in range(y,y+1) for z1 in range(z,z+1)]
print(A)

A = [(y,x) for x in [1,2,3]  for y in [1,2,3]]
print(A)