# -*- coding: utf-8 -*-
"""
Created on Thu Feb 15 22:10:34 2018

@author: lokesh.r

Reduce functionlaity without using buildin function reduce[functools]
"""
#reduce function
def red(v1,v2):
    return v1+v2
def reduce(alist):
    tot = 0
    for i in range(len(alist)):
        tot = red(tot,alist[i])
    print(tot)

lista =[10,2,25,4,15,6,67]
reduce(lista)

# Filter Function
def fil(val):
    return val%2
result=[]
def filter(alist):
    for i in alist:
        result.append(fil(i))
    print(result)
filter(lista)