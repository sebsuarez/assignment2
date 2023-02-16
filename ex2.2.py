import sys
import timeit
import json
import matplotlib.pyplot as plt

sys.setrecursionlimit(20000)

def func1(arr, low, high):
    if low < high:
        pi = func2(arr, low, high)
        func1(arr, low, pi-1)
        func1(arr, pi + 1, high)

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

def main():
    with open("file.json") as file:
        data = json.load(file)

    time_arr = []
    length= []
    for i in range(len(data)):
        length.append(len(data[i]))
        func1(data[i], 0, len(data[i])-1)
        time = timeit.timeit(lambda:func1(data[i], 0, len(data[i])-1), number=1)
        time_arr.append(time)

    plt.plot(range(10),time_arr)
    plt.ylabel('Time (sec)')
    plt.xlabel('Data set')
    plt.title('Timing')
    plt.show()

main()