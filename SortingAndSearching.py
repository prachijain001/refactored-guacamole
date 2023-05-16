class Searching:
    def __init__(self, arr):
        self.arr = arr

    # Linear search algorithm
    def linear_search(self, item):
        for i in range(len(self.arr)):
            if self.arr[i] == item:
                return i
        return -1

    # Binary search algorithm (assumes that the array is sorted)
    def binary_search(self, item):
        low = 0
        high = len(self.arr) - 1
        while low <= high:
            mid = (low + high) // 2
            if self.arr[mid] == item:
                return mid
            elif self.arr[mid] < item:
                low = mid + 1
            else:
                high = mid - 1
        return -1

#Sorting Algorithms
class Sorting:
    def __init__(self, arr):
        self.arr = arr


    # Quick sort algorithm
    def quick_sort(self, arr=None):
        if arr is None:
            arr = self.arr

        if len(arr) <= 1:
            return arr

        pivot = arr[len(arr) // 2]
        left_half = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right_half = [x for x in arr if x > pivot]

        return self.quick_sort(left_half) + middle + self.quick_sort(right_half)


    # Insertion sort algorithm
    def insertion_sort(self):
        for i in range(1, len(self.arr)):
            key = self.arr[i]
            j = i - 1
            while j >= 0 and key < self.arr[j]:
                self.arr[j + 1] = self.arr[j]
                j -= 1
            self.arr[j + 1] = key
            
    #display
    def display(self):
        print(self.arr)

a=int(input("Number of elements in the array:- "))
arr=list(map(int, input("Enter elements of array:- ").strip().split()))
print(arr)

sorting = Sorting(arr)
searching = Searching(arr)

# Linear search
key=int(input("Element to be searched:- "))
print("Element found at index ",(searching.linear_search(key)))

# Binary search
key=int(input("Element to be searched:- "))
sorting.bubble_sort()
print("Element found at index:- ",(searching.binary_search(key)))

# Bubble sort
sorting.bubble_sort()
print("After Bubble Sort ")
sorting.display()

# Selection sort
sorting.selection_sort()
print("After Selection Sort ")
sorting.display()

# Merge sort
sorting.merge_sort()
print("After Merge Sort")
sorting.display()

# Quick sort
sorted_arr = sorting.quick_sort()
print("After Quick Sort")
print(sorted_arr)

# Insertion sort
sorting.insertion_sort()
print("After Insertion Sort ")
sorting.display()
