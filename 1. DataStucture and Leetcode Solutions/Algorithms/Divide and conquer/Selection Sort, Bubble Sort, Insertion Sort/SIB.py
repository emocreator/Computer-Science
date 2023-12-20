"""
Reference: https://www.youtube.com/@BroCodez

Insertion Sort

Insertion sort is an in-place comparison sorting algorithm that directly modifies the input data without requiring additional space.
It has a time complexity of O(n^2), making it inefficient for large lists, similar to selection sort.
While insertion sort also has a time complexity of O(n^2) in the average and worst cases, it generally performs better than selection sort
on smaller datasets due to its more efficient constant factors and its adaptive nature when dealing with nearly sorted or partially sorted
arrays. The main principle behind insertion sort is to build the sorted array one element at a time by repeatedly taking the next element
and inserting it into its correct position within the already sorted part of the array. Despite being less efficient for larger lists,
insertion sort is valued for its simplicity and efficiency on smaller or nearly sorted arrays.

Algorithm Pseudocode:
InsertionSort(arr):
    n = length of arr
    
    for i from 1 to n-1:
        key = arr[i]
        j = i - 1
        
        // Move elements of arr[0..i-1] that are greater than key to one position ahead of their current position
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j = j - 1
        
        arr[j + 1] = key

Selection Sort Algorithm


Selection sort, an in-place comparison sorting algorithm, operates directly on the input data without the need for extra space. It exhibits a time complexity of O(n^2),
rendering it less efficient on larger datasets. While generally performing worse than insertion sort due to its higher time complexity, selection sort is appreciated for
its straightforward and easy-to-understand implementation. It systematically sorts the array by repeatedly finding the minimum element from the unsorted portion and placing
it at the beginning. Despite its inefficiency with larger datasets, selection sort remains notable for its simplicity in implementation and understanding.

Algorithm Pseudocode:
SelectionSort(arr):
    n = length of arr
    
    for i from 0 to n-1:
        min_index = i
        
        for j from i+1 to n:
            if arr[j] < arr[min_index]:
                min_index = j
        
        if min_index != i:
            swap arr[i] with arr[min_index]

Bubble Sort Algorithm

Bubble sort is an in-place comparison sorting algorithm that operates directly on the input data without requiring additional space. It features a time complexity of O(n^2),
which makes it less efficient,especially on larger datasets. In comparison to both insertion sort and selection sort, bubble sort often performs less favorably due to its inherent inefficiency.
The essence of bubble sort lies in its repetitive traversal through the array, where adjacent elements are compared and swapped if they are in the incorrect order. This process continues until
the entire array is sorted. Despite its simplicity and ease of implementation, bubble sort's time complexity, particularly on larger lists, makes it less suitable for practical applications where efficiency is crucial.

Algorithm Pseudocode:
BubbleSort(arr):
    n = length of arr
    
    for i from 0 to n-1:
        swapped = False
        for j from 0 to n-i-1:
            if arr[j] > arr[j+1]:
                Swap arr[j] with arr[j+1]
                swapped = True
        
        if swapped is False:
            break  // If no elements were swapped in this pass, the array is already sorted

"""

class Sort:

    @staticmethod
    def selectionsort(x):
        n = len(x) # Length of array
        
        for i in range(n-1):
            min_index = i
            
            for j in range(i+1,n):
                if x[j]<x[min_index]:
                   min_index=j
                   
            if min_index != i:
                x[i],x[min_index]=x[min_index],x[i]
                
        return x
    
    @staticmethod
    def insertionsort(x):
        n = len(x)

        for i in range(1,n):
            min_index = x[i]
            temp = i-1
            
            while temp>=0 and min_index< x[temp]:
                x[temp+1] = x[temp]
                temp-=1
                
            x[temp+1] = min_index
            
        return x

    @staticmethod
    def bubblesort(x):
        n = len(x)
        
        for i in range(n-1):
            swap = False
            
            for j in range(0,n-i-1):
                if x[j] > x[j+1]:
                    x[j],x[j+1]= x[j+1],x[j]
                    swap = True
                    
            if swap == False:
                break
            
        return x

if __name__ == '__main__':
    unsorted_array = [10,5,2,4,36,152,4,5,7,1,5,235,12,4,412,1231,2,14,12,1,2,1,23,12,31,2,3,2232,2322223,231]
    print(Sort.selectionsort(unsorted_array))
    print(Sort.insertionsort(unsorted_array))
    print(Sort.bubblesort(unsorted_array))
