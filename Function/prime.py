def check_prime(num):
    if num == 2:
        return True
    else:
        for i in range(2, int(num / 2) + 1):
            if num % i == 0:
                return False
        return True


def main():
    while True:
        start, stop = tuple(map(int, input("Enter a range : ").split()))
        if start >= 2 and (2 <= stop <= 100):
            break
    for i in range(start, stop + 1):
        if check_prime(i):
            print(i, end=" ")


if __name__ == "__main__":
    main()
