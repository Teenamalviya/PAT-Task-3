# Problem: 2

# Given List
list_given = [10,501,22,37,100,999,87,351]
primes = []
# Iterate over the given list
for num in list_given:
# Check the factors of number upto half of its value and if modulus of number not equals to zero then its prime number
    for i in range(2, int((num/2)+1)):
        if (num % i) == 0:
            break
        else:
            primes.append(num)
            break
# Print  total number of prime numbers and its list
print("Number of Prime numbers in list:", len(primes))
print("Prime List:",primes)