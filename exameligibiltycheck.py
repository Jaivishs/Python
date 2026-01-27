med = input("Do you have any serious medical issues that could prevent you from taking the test (Y or N)?:  ")
att = int(input("Enter your attendance in percent: "))

if med == "Y":
    print("You are not allowed")
else:
    if att>=75:
        print("You are allowed to take the exam")
    else:
        print("Not allowed")