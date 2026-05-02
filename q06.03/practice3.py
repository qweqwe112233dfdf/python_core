import random

nums = [random.randint(1, 100) for _ in range(100)]

def min_sum_index(arr, i=0, min_i=0, min_sum=None):
    if i > len(arr) - 10:
        return min_i

    current_sum = sum(arr[i:i+10])

    if min_sum is None or current_sum < min_sum:
        return min_sum_index(arr, i + 1, i, current_sum)
    else:
        return min_sum_index(arr, i + 1, min_i, min_sum)

print(nums)
print(min_sum_index(nums))