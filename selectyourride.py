print("Select your ride")
print("1) Bike")
print("2) Car")

choice = int(input("Enter your choice by typing 1 or 2: "))

if choice == 1:
    print("What type of bike?")
    print("1 - motorbike")
    print("2 - cycle")
    choice2 = int(input("Enter your choice by typing 1 or 2: "))
elif choice == 2:
    print("What type of car?")
    print("1 - Sedan")
    print("2 - SUV")
    choice3 =int(input("Enter your choice by typing 1 or 2: "))

    if choice3 == 1:
        print("Wow, that was a good choice!")
    elif choice3 == 2:
        print("That is quite a good car!")
    else:
        print("Are you sure that you entered either 1 or 2?")
else:
    print("Are you sure that you entered either 1 or 2?")
