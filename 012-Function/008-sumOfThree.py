def sum_of_num(*nums):
    total = 0
    for i in nums:
        total += i
    return total


print(sum_of_num(1, 3, 4, 5, 6))
