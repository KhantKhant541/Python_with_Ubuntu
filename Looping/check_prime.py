while True:
    n = int(input("Enter a positive integer : "))

    if n > 0:
        break

temp = int(n / 2)
if n == 1:
    print(f"{n}  is not a prime number.")

elif n == 2 or n == 3:
    print(f"{n} is a prime number.")

else:
    for i in range(2, temp + 1):
        if n % i == 0:
            print(f"{n} is not a prime number.")
            break

        else:
            print(f"{n} is a prime number.")
            break
