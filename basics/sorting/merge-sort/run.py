#!/usr/bin/env python3

""" Runner for merge sort tests """

import unittest
from mergesort import MergeSort

class MergeSortTests(unittest.TestCase):
    
    def test_empty(self):
        input = []

        expected = []
        actual = MergeSort().sort(input)

        self.assertEqual(expected, actual)

    def test_single_value(self):
        input = [1]

        expected = [1]
        actual = MergeSort().sort(input)

        self.assertEqual(expected, actual)

    def test_unsorted_values(self):
        input = [3,1,2]

        expected = [1,2,3]
        actual = MergeSort().sort(input)

        self.assertEqual(expected, actual)

    def test_unsorted_values_with_duplicates(self):
        input = [3,1,2,2]

        expected = [1,2,2,3]
        actual = MergeSort().sort(input)

        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()