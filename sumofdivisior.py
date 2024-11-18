n = 4
sum = 0
for num in range(1, n + 1):
    if n % num == 0:
        sum = sum + num
        print(num)

# print(sum)