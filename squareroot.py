num = float(input("Enter a number to find the square root: "))
sq_root = num ** 0.5

if num < 0:
    print("The square root of a negative number is not possible")
else:
    print(f"The square root of {num} is {sq_root}")

