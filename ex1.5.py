import timeit
import matplotlib.pyplot as plt

def memo(n, memo_dict={}):
    if n in memo_dict:
        return memo_dict[n]
    elif n == 0 or n == 1:
        return n
    else:
        result = memo(n-1, memo_dict) + memo(n-2, memo_dict)
        memo_dict[n] = result
        return result


def main():
    memo_arr = []
    for i in range(36):
        memo_time = timeit.timeit(lambda: memo(i), number = 10000)
        memo_arr.append(memo_time)
        i += 1
    plt.plot(range(36), memo_arr)
    plt.title("Improved Code Performance")
    plt.ylabel("Computation Time (seconds)")
    plt.xlabel("n (iterations)")
    plt.show()

main()