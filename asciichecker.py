print("ASCII value checker")
print("=" * 40)

ch = input("Enter any one character: ")

if type(ch) is str and len(ch)==1:
    asciinum = ord(ch)
    print(f"Character: {ch}")
    print(f"The ASCII value of this is {asciinum}")

    print("\nCharacter Type: ", end="")

    if asciinum >= 65 and asciinum <=90:
        print("The character is an uppercase letter")
    elif asciinum >= 97 and asciinum <122:
        print("The character was a lowercase letter")
    elif asciinum >=48 and asciinum <= 57:
        print("The character is a digit")
    elif asciinum == 32:
        print("The character is a space")
    else:
        print("The character is a special character")
else:
    print("Make sure you only printed ONE character")