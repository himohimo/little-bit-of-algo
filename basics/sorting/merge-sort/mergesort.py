#!/usr/bin/env python3

""" Merge sort """

from typing import List

class MergeSort():

    def sort(self, arr: List[int]) -> List[int]:
        
        if arr is None or len(arr) == 0:
            return []
        
        if len(arr) == 1:
            return arr

        mid = len(arr) // 2

        l_arr = self.sort(arr[:mid])
        r_arr = self.sort(arr[mid:])
        result_arr = []

        l_idx = 0
        r_idx = 0

        while l_idx < len(l_arr) and r_idx < len(r_arr):

            if l_arr[l_idx] == r_arr[r_idx]:
                result_arr.append(l_arr[l_idx])
                result_arr.append(r_arr[r_idx])
                l_idx += 1
                r_idx += 1

            elif l_arr[l_idx] < r_arr[r_idx]:
                result_arr.append(l_arr[l_idx])
                l_idx += 1
            else:
                result_arr.append(r_arr[r_idx])
                r_idx += 1

        if l_idx < len(l_arr):
            result_arr.extend(l_arr[l_idx:])

        if r_idx < len(r_arr):
            result_arr.extend(r_arr[r_idx:])

        return result_arr
