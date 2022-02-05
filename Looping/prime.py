
n = int(input("Enter a positive integer : "))

if_prime = True
i = 2
while if_prime:
    if i < n:
        if n % i == 0:
            if_prime = False
    else:
        break
    i += 1

if not if_prime:
    print("It is not a prime number.")
else:
    print("It is a prime number.")
