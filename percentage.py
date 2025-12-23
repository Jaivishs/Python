print("Please enter your marks obtained in 4 subjects: ")
maths = int(input("Maths: "))
english = int(input("English: "))
science = int(input("Science: "))
hindi = int(input("Hindi: "))

sum = maths+english+science+hindi
print("The sum of the 4 subjects out of 400 is: ", sum)

percentage = sum/4
print(end="Percentage mark: ")
print(percentage,"%")