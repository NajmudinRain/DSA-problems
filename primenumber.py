class PrimeNumber:
<<<<<<< HEAD
    def checkprimeNumber(self, n):

        count = 0
        i = 1
        while i * i <=n:
            if n % i == 0:
                count+=1
                #the other factor has to be different. for example: 1. this case of for perfect sqaure number
                if (n/i)!=i:
                    count+=1
            i+=1
        if count == 2:
            return True
        else:
            return False



if __name__ == "__main__":
    obj = PrimeNumber()
    for i in range(40):
        print(i, obj.checkprimeNumber(i))

    # print(obj.checkprimeNumber(16))
=======
    # def checkprimeNumber(self, n):
    #
    #     count = 0
    #     i = 1
    #     while i * i <=n:
    #         if n % i == 0:
    #             count+=1
    #             #the other factor has to be different. for example: 1. this case of for perfect sqaure number
    #             if (n/i)!=i:
    #                 count+=1
    #         i+=1
    #     if count == 2:
    #         return True
    #     else:
    #         return False

    #another way to check - prime
    def check_prime(self,num):

        if num <= 1:
            return False
        for i in range(2,int(num ** 0.5) + 1):
            if num % i:
                return False
        return True

    def prime_num_tillnum(self, num):
        #one way is iterate over the number and check one by one if its prime or not(to check write one function)
        #the another way is sieve of erastothenes
        primes = [True] * (num + 1)
        primes[0] = primes[1] = False
        for i in range(2, int(num ** 0.5)+1):
            if primes[i]:
                for j in range(i * i, num+1, i):
                    primes[j] = False
        for i, num in enumerate(primes):
            print(f"{i}-->{num}")

# Time Complexity:
# O(nloglog(n))
# Space Complexity:
# 𝑂(𝑛)


obj = PrimeNumber()
# print(obj.checkprimeNumber(16))
print(obj.prime_num_tillnum(10))
>>>>>>> 51dc26c (problems solution dsaI)
