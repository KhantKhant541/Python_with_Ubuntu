def square_fun(x):
    """This function return square of any number"""
    return x ** 2


num = int(input("Enter a number : "))
print(f"Square of {num} : {square_fun(num)}")
print(square_fun.__doc__)
