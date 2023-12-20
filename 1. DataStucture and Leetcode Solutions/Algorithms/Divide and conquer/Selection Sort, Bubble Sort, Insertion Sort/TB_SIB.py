import unittest
import random
from SIB import Sort

class TestSortingAlgos(unittest.TestCase):

    def test_selection_sort(self):
        arr = self.generate_random_list(100, 1000)
        self.check_sorted(Sort.selectionsort(arr))

    def test_insertion_sort(self):
        arr = self.generate_random_list(100, 1000)
        self.check_sorted(Sort.insertionsort(arr))

    def test_bubble_sort(self):
        arr = self.generate_random_list(100, 1000) 
        self.check_sorted(Sort.bubblesort(arr))

    def test_nearly_sorted(self):
        arr = [1, 2, 3, 5, 4, 6, 7, 8]
        self.check_sorted(Sort.insertionsort(arr))

    def generate_random_list(self, n, max_val):
        lst = []
        for _ in range(n):
            lst.append(random.randint(0, max_val))
        return lst

    def check_sorted(self, arr):
        for i in range(len(arr)-1):
            self.assertTrue(arr[i] <= arr[i+1])

if __name__ == '__main__':
    unittest.main()
