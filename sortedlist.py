# Problem 8:

# Create a list
list1 = [7, 8, 6, 9, 5]
# Total number of elements in a list
totalelements = len(list1)

# consider first element in a list as minimum element
min_element = list1[0]
# Iterate over the given list
for i in range(totalelements):
# Compare the first element in the list with other elements
    if list1[i] < min_element:
        min_element = list1[i]
# Print the minimum element in the list
print("The minimum element in the list:",min_element)