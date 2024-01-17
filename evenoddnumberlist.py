# Problem: 1

# The given list
list_given = [10,501,22,37,100,999,87,351]
# Create even and odd empty list
list_even = []
list_odd =[]
# Loop over the given list
for l in list_given:
# If modulus of the number equal to 0 then its even otherwise its odd
    if l%2 ==0:
        list_even.append(l)
    else:
        list_odd.append(l)
# Print even and odd lists
print("Even List:",list_even)
print("Odd List:",list_odd)