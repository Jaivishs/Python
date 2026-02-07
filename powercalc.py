num = int(input("Enter a number"))
power = int(input("Enter the power to which you want to raise the number by"))

for i in range(1, power+1):
    answer = num ** i
    print(f"{num} to the power of {i} is {answer}")