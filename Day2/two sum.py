# -*- coding: utf-8 -*-
"""
Created on Sun Nov 19 14:19:04 2023
@author: Kulsoom
"""


def twoSum(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i]+nums[j] == target:
                return ([i,j])


print(twoSum([3,2,4],6))