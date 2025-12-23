amount = int(input("Please enter the amount of rupees for withdrawal:  "))

note_1 = amount//100
note_2 = (amount%100)//50
note_3= ((amount%100)%50)//10

print("The amount of 100 rupee notes needed is: ", note_1)
print("The amount of 50 rupee notes needed is: ", note_2)
print("The amount of 10 rupee notes needed is: ", note_3)
