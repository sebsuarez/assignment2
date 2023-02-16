import timeit

def func(n):
    if n == 0 or n == 1:
        return n
    else:
        return func(n-1) + func(n-2)

def memo(n, memo_dict={}):
    # For the function, it checks if n is already in the memo dictionary.
    # By doing this, it will not have to compute the "memoized" functions again.
    # In summary, when we make recursion look like a tree, the tails will be the same computation.
    # Instead of computing the same step many times, we will check if it has been computed and return that value.
    if n in memo_dict:
        return memo_dict[n]
    elif n == 0 or n == 1:
        return n
    else:
        result = memo(n-1, memo_dict) + memo(n-2, memo_dict)
        memo_dict[n] = result
        return result

print("\n\nNow computing when n = 15.")
result1 = timeit.timeit(lambda: func(15), number = 10000)
print(f"\nThe result using func()is: {result1:.8}")
result2 = timeit.timeit(lambda: memo(15), number = 10000)
print(f"The result using memo()is: {result2:.8}")

print("\n\nNow computing when n = 18.")
result3 = timeit.timeit(lambda: func(18), number = 10000)
print(f"\nThe result using func()is: {result3:.8}")
result4 = timeit.timeit(lambda: memo(18), number = 10000)
print(f"The result using memo()is: {result4:.8}\n")
