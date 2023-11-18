# -*- coding: utf-8 -*-
"""
Created on Sat Nov 18 19:51:00 2023
@author: Kulsoom
"""
def merge_lists_in_order(lis1, lis2):
    lis1_index = 0
    lis2_index = 0
    for i in range(lis1_index, len(lis1)):
        for j in range(lis2_index, len(lis2)):
            if lis1[i]>lis2[j]:
                print(lis2[j])
                lis2_index = lis2_index+1
            elif lis1[i]<lis2[j]:
                break
        print(lis1[i])
        lis1_index = lis1_index+1
        
    # If there are remaining elements in lis2, print them
    while lis2_index < len(lis2):
        print(lis2[lis2_index])
        lis2_index += 1

lis1 = [1,4,6,9,11,12]
lis2 = [0,3,5,8,10,13,14]  
         
merge_lists_in_order(lis1, lis2)
