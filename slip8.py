#QUESTION 1
my_set = {1, 2, 3, 4, 5}
total = sum(my_set)
average = total / len(my_set)
print("Average : ", average)



#QUESTION 2
def multiply_list(numbers):
    result = 1
    for num in numbers:
        result *= num
    return result

# Example usage
my_list = [8, 2, 3, -1, 7]
result = multiply_list(my_list)
print("Product of elements in list is : ",result)