#QUESTION 1
def str_len(string):
    count = 0
    for char in string:
        count += 1
    return count

input_string = input("Enter a string: ")
length = str_len(input_string)
print("Length of the string:", length)


#QUESTION 2
n = int(input("Enter the number of elements: "))
numbers = []

for i in range(n):
    num = int(input("Enter a number: "))
    numbers.append(num)

# Remove duplicates using set()
unique_numbers = list(set(numbers))

print("Original list:", numbers)
print("List after removing duplicates:", unique_numbers)
