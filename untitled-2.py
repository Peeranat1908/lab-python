number = int(input())
i = 0
if number > 0:
    while number > 2:
        i = number % 10
        number = number // 10
        print(i)
else:
    print("ERROR")