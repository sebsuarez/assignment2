import sys
import timeit
import matplotlib.pyplot as plt
import json

sys.setrecursionlimit(20000)


def func1(arr, low, high):
    if low < high:
        pivot_index = func2(arr, low, high)
        func1(arr, low, pivot_index-1)
        func1(arr, pivot_index + 1, high)

def func2(array, start, end):
    p = array[start] 
    low = start + 1 
    high = end      
    while True:
        while low <= high and array[high] >= p:     
            high = high - 1
        while low <= high and array[low] <= p:      
            low = low + 1
        if low <= high:
            array[low], array[high] = array[high], array[low]
        else:
            break
    array[start], array[high] = array[high], array[start]
    return high

def sort(arr, low, high):
    if low < high:
        pivot_index = partition(arr, low, high)
        sort(arr, low, pivot_index - 1)
        sort(arr, pivot_index + 1, high)
    return

def partition(array, start, end):
    p = array[(start + end)//2] 
    low = start + 1 
    high = end      
    while True:
        while low <= high and array[high] >= p:    
            high = high - 1
        while low <= high and array[low] <= p:      
            low = low + 1
        if low <= high:
            array[low], array[high] = array[high], array[low]
        else:
            break
    array[start], array[high] = array[high], array[start]
    return ((high + low )//2)

def default_func(i, arr):
    unoptimized = func1(arr[i], 0, len(arr[i])-1)
    return unoptimized

def better_func(i, arr):
    optimized = sort(arr[i], 0, len(arr[i])-1) 
    return optimized

def main():
    with open("file.json", "r") as file:
        arr = json.load(file)

    optimized_y = []
    array_x = []

    for i in range(len(arr)):
        times1 = timeit.timeit(lambda: better_func(i, arr), number=1)
        optimized_y.append(times1)
        array_x.append(len(arr[i]))

    unopt_arr = []
    array_x = []

    for i in range(len(arr)):
        times2 = timeit.timeit(lambda: default_func(i, arr), number=1)
        unopt_arr.append(times2)
        array_x.append(len(arr[i]))
    plt.plot(array_x, optimized_y, label = "Optimized Version")
    plt.plot(array_x, unopt_arr, label = "Original Version")
    plt.xlabel('n (numer of elements)')
    plt.ylabel('Computing Time (seconds)')
    plt.legend()
    plt.show()
main()