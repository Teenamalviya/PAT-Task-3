# Program: 10

# Given list
input_list = [4,2,-3,1,6]
# Given value
k=0
# Sort the list
input_list.sort()
result = []
# Iterate the list upto two element less
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
if len(result)>0:
    print("There is a sub-list in list whose sum equal to zero",result)
else:
    print("There is no sub-list whose sum equal to zero")