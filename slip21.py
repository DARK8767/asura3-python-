# Define a tuple
tup1 = (1, 'apple', 3.14)
var1, var2, var3 = tup1

# Display the unpacked variables
print("var1 : ", var1)
print("var2 : ", var2)
print("var3 : ", var3)



#QUESTION 2
numbers = []

# Accept 6 integer values
for _ in range(6):
    num = int(input("Enter an integer: "))
    numbers.append(num)

# Check for duplicates
if len(numbers) != len(set(numbers)):
    print("DUPLICATES")
else:
    print("ALL UNIQUE")
