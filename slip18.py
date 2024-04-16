#QUESTION 1
calculate_area = lambda side: side ** 2

side = int(input('Enter the side of square : '))
area = calculate_area(side)
print(f"AREA OF SQUARE WITH SIDE {side} is : ",area)




#QUESTION 2
def cnt_freq(string):
    frequency = {}
    for char in string:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    return frequency

string = input("Enter a string: ")
chars = cnt_freq(string)

for char, count in chars.items():
    print(f"Character '{char}' appears {count} times.")
