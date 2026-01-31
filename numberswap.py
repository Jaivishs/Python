a = int(input("Enter the first number: "))
b = int(input("Enter the second numbes: "))
c = int(input("Enter the third number: "))

a2 = str(input("What is the real value of a(enter b or c): "))
b2 = str(input("What is the real value of a(enter a or c): "))
c2 = str(input("What is the real value of a(enter b or a): "))

if a == "b2":
    if b == "c2":
        a, b, c = b, c, a
    else:
        a, b = b, a
elif a == "c2":
    if b == "a2":
        a, b, c = c, a, b
    else:
        a, c = c, a

print("After swapping:")
print(f"a = {a}, b = {b}, c = {c}")
