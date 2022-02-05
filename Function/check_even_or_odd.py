def check_even_odd(n):
    if n % 2 == 0:
        return True
    else:
        return False


n = int(input("Enter a positive integer : "))
if check_even_odd(n):
    print("Even")
else:
    print("Odd")
