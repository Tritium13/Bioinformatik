a = int(input("a: "))
b = int(input("b: "))
sum = 0


for i in range(a, b + 1):
    if i % 2 == 1:
        sum += i
        print(sum)