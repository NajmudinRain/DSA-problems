0,1,1,2,3,5,8,13,21
class Fibo:
    def fib(self, n):
        """

        :type n: int
        :rtype: int


        """
        # if n <= 1:
        #     return n

        # prev1 = 0
        # prev2 = 1

        # for count in range(2, n+1):
        #     current = prev1 + prev2
        #     prev1 = prev2
        #     prev2 = current

        # return current

        if n <= 1:
            return n
        return self.fib(n - 1) + self.fib(n - 2)

obj = Fibo()
print(obj.fib(7))





