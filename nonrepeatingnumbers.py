# Problem: 7

#Given List
list1 = [1,2,3,2,4]
a = []
# Iterate over the list
for num in list1:
# Check whether num is present in a unique list
    if num in a:
        a.remove(num)
    else:
        a.append(num)
# Print the non-repeating numbers list
print("Non-repeating numbers in a list:",a)
