#QUESTION 1
calculate_area = lambda side: side ** 2

side = int(input('Enter the side of square : '))
area = calculate_area(side)
print(f"AREA OF SQUARE WITH SIDE {side} is : ",area)


#QUESTION 2
string = input('Enter any string : ')

char_counts = {}
for char in string:
    char_counts[char] = char_counts.get(char, 0) + 1

print("CHARACTER COUNT IN THE STRING : ", char_counts)
