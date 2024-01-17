# Problem: 3

# Given List
list_given = [10,501,22,37,100,999,87,351]
happynumbers = []
#Iterate over the list
for i in range (len(list_given)):
    sum = list_given[i]
# Run the while loop until number not equals to 1 or 4
    while sum!=1 and sum !=4:
        tempsum = 0
# Iterate over the digits of the number
        for digit in str(sum):
# Assign the sum of squares to temporary variable
            tempsum += int(digit) ** 2
        sum = tempsum
# If sum of digits equals to 1, then the number is happy number and add it to the happy number list
    if sum == 1:
        happynumbers.append(list_given[i])
# Print happy number list
print(happynumbers)