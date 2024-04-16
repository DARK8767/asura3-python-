#QUESTION 1
nterms = int(input ("How many terms the user wants to print? "))  
n1 = 0  
n2 = 1  
count = 0  
if nterms <= 0:  
    print ("Please enter a positive integer, the given number is not valid")  
elif nterms == 1:  
    print ("The Fibonacci sequence of the numbers up to", nterms, ": ")  
    print(n1)  
else:  
    print ("The fibonacci sequence of the numbers is:")  
    while count < nterms:  
        print(n1)  
        nth = n1 + n2  
        n1 = n2  
        n2 = nth  
        count += 1 


#QUESTION 2
n = int(input("Enter a number: "))

# Generate the dictionary using a dictionary comprehension
result_dict = {x: x*x for x in range(1, n+1)}

# Print the dictionary
print(result_dict)
