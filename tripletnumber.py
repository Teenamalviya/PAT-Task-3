# Problem: 9

# The given list
input_list = [10,20,30,9]
# The given value
k=59
# Sort the list
input_list.sort()
result = []
# Iterate over the list
for i in range(len(input_list) - 2):
    left = i + 1
    right = len(input_list) - 1
    while left < right:
        if input_list[i] + input_list[left] + input_list[right] == k:
            result.append((input_list[i], input_list[left], input_list[right]))
            left += 1
            right -= 1
        elif input_list[i] + input_list[left] + input_list[right] < k:
            left += 1
        else:
            right -= 1
# Print the substring whose sum equal to 59
print("The sum of the substring whose sum is 59: ",result)