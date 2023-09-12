

def find_prime_numbers(nums):
    prime_nums = []
    for i in nums:
        if i % 3 == 0 and i % 5 == 0:
            prime_nums.append(i)
    return sum(prime_nums)

nums = [i for i in range(1000)]

sum_nums = find_prime_numbers(nums)

print(sum_nums)
