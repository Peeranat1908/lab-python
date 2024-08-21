while True:
    n = int(input("Enter a number: "))
    i = 1
    c = 0
    if n == 0:
        print("End of program, goodbye.")
        break
    if n > 1:
        if i <=  n :
            if n % i == 0:
                c += 1
            i += 1
        if c == 2:
            print(f"{n} is not prime number.")
        else:
            print(f"{n} is prime number.")
    else:
        print("Invalid input, try again.")
        continue