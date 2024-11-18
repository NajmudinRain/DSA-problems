class HCF:
    def hcf(self, n1, n2):
        gcd = 1
        for i in range(1,min(n1,n2)+1):
            if n1 % i ==0 and n2 % i == 0:
                gcd = i
        return gcd

    def lcm(a, b):
        # Start with the larger of the two numbers
        multiple = max(a, b)

        # Keep checking multiples of the larger number until you find one divisible by the smaller number
        while multiple % a != 0 or multiple % b != 0:
            multiple += max(a, b)

        return multiple

    def hcf_euclidean(self, n1, n2):
        while n2 != 0:
            n1, n2 = n2, n1%n2
        return n1



    # def hcf_euclidean(self, n1, n2):
    #     while n2 != 0:
    #         n1, n2 = n2, n1%n2
    #     return n1

    # def lcm_euclidean(self, n1, n2):
    #     # LCM formula using GCD
    #     return abs(n1 * n2) // gcd(n1, n2)

if __name__ == "__main__":
    obj = HCF()
    print(obj.hcf(10,20))



