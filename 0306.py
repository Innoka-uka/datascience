import random
import time

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]


def test_sort(sort_func, sizes=[100, 1000, 10000]):
    for size in sizes:
        arr = [random.randint(0, 10000) for _ in range(size)]
        start_time = time.time() 
        sort_func(arr) 
        end_time = time.time() 
        
        print(f"数列长度{size}, 用时 {end_time - start_time:.2f} seconds")

test_sort(selection_sort)