mean1 = 38
totnum = 40
wrongnum = 36
correctnum = 56

sum = mean1*totnum
print(f"The sum of 40 numbers is {sum}")

correctsum = sum + ((correctnum)-(wrongnum))
print(f"The correct sum of all of the numbers is {correctsum}")

mean2 = correctsum/totnum
print(f"The actual mean of the numbers is {mean2}")