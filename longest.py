# -*- coding: utf-8 -*-
"""
Created on Mon Feb 26 22:24:39 2018

@author: lokesh.r
"""

words = ["jupyter","python","java", "trignometry","calculus","packedwater"]
#x = max([len(i) for i in words])
y ={z for z in words if len(z) == max([len(i) for i in words])}
print(set(y))

  
    
    