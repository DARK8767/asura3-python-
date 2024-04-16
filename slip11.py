#QUESTION 1
def contains_all_vowels(string):
    vowels = set('aeiou')
    return vowels.issubset(string.lower())

# Example usage
input_string = input("Enter a string: ")
if contains_all_vowels(input_string):
    print("The string contains all vowels.")
else:
    print("The string does not contain all vowels.")

#QUESTION 2
def rev(number):
    rev_num = int(str(number)[::-1])
    return rev_num

input_number = int(input("Enter a number: "))
reverse = rev(input_number)
print("Reversed number:", reverse)