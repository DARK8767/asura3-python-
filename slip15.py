#QUESTION 1
def is_palindrome(string):
    reversed_string = string[::-1]
    if string == reversed_string:
        return True
    else:
        return False

input_string = input("Enter a string: ")
if is_palindrome(input_string):
    print("The string is palindrome.")
else:
    print("The string is not palindrome.")



#QUESTION 2
def sum_of_digits(number):
    sum_digits = 0
    while number > 0:
        digit = number % 10  # Get the last digit
        sum_digits += digit  # Add the digit to the sum
        number //= 10  # Remove the last digit
    return sum_digits

input_number = int(input("Enter a number: "))
digit_sum = sum_of_digits(input_number)
print("Sum of digits:", digit_sum)