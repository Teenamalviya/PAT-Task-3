# Problem: 4

# Enter the user input
num = input("Enter number : ")
# Assign the digit of the number to the list
first_digit = int(num[0])
# Assign the last digit of the number to the list
last_digit = int(num[-1])
# Add the both digits
sum = first_digit + last_digit
# Print the sum of both digits
print("Sum of first and last digit:", sum)
