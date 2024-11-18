class Problems:
    def printnamesntimes(self, n):
        if n == 0:
            return
        print("NajmudinRain")
        self.printnamesntimes(n-1)

    def printfrom1ton(self, n):
        if n == 0:
            return
        self.printfrom1ton(n-1)
        print(n, end= " ")

    def printfromNto1(self, n):
        if n == 0:
            return
        print(n, end=" ")
        self.printfromNto1(n-1)

    def factorialn(self,n):
        if n < 0:
            print("enter positive integer")
            return
        if  n == 1 or n == 0:
            return 1
        return n * self.factorialn(n-1)

    def factorail_forloop(self, n):
        fact = 1
        for i in range(1,n+1):
            fact = i * fact
        return fact


    def reverselist(self, arr):
        i = 0
        j = len(arr) - 1
        while i <= j:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1


    def reverselistrecurrsion(self, arr):
        start = 0
        end = len(arr) - 1

        #we con do this by using one argument as well. by using start and len of string
        self.reverse(arr, start, end)

    def reverse(self, arr, start, end):

        if (start >= end):
            return
        arr[start], arr[end] = arr[end], arr[start]
        self.reverse(arr, start + 1, end - 1)



if __name__ == "__main__":
    obj = Problems()
    obj.printnamesntimes(5)
    obj.printfrom1ton(10)
    # obj.printnamesntimes(5)
    # obj.printfrom1ton(10)
    print(obj.factorialn(0))
    print(obj.factorail_forloop(0))
    # li = [1, 2, 3, 4, 5]
    # obj.reverselist(li)
    # print(li)
