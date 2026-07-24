print("Hello, I am an AI bot. What is your name? \n")
name = str(input())
print(f"Nice to meet you, {name}")

print("How are you feeling today? (Good/Bad). /n")
mood = input().lower()

if mood == "good":
    print("Nice to hear that!")
elif mood == "bad":
    print("Sorry to hear that")
else:
    print("Please enter either good or bad")