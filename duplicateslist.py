# Problem: 6

# Create three list
list1 = [1, 2, 3, 4, 5, 6, 7]
list2 = [4, 5, 8, 3]
list3 = [3, 4, 5, 8, 10]
duplicate = []
# Iterate over the first list
for num in list1:
# Check the first list number in other two lists
    if num in list2 and num in list3:
        duplicate.append(num)
# Print duplicates numbers in the three lists
print("Duplicates in the list:",list(set(duplicate)))