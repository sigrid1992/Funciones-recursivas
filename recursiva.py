# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 11:22:49 2021

@author: sigri
"""
def recursiva(num):
    print("Valor Inicial ->",num)
    
    if num > 1:
        num = num * recursiva(num -1)
    print("valor final ->",num)
    return num

print(recursiva(6))
    