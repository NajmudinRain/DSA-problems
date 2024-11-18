def checkprimeNumber(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def prime_num_tillnum(num):
    # one way is iterate over the number and check one by one if its prime or not(to check write one function)
    # the another way is sieve of erastothenes
    prime_nums = [True] * (num + 1)
    prime_nums[0] = False
    prime_nums[1] = False
    for i in range(2, int(num ** 0.5) + 1):
        if prime_nums[i]:
            for j in range(i * i, num + 1, i):
                prime_nums[j] = False
    ans = [i for i, prime in enumerate(prime_nums) if prime]
    return ans


def first_n_prime_numer(num):
    prime_nums = [2]
    n = 3
    while len(prime_nums) < num:
        if is_prime(n, prime_nums):
            prime_nums.append(n)
        n= n+2
    return  prime_nums


def is_prime(n, prime_nums):
    for prime in prime_nums:
        if prime * prime > n:
            break
        if n % prime == 0:
            return False
    return True

if __name__ == "__main__":
    print(prime_num_tillnum(100))
    print(first_n_prime_numer(10))





