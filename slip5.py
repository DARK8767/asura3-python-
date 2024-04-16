#QUESTION 1
T = (4, 2, 6.8, 1.8, 10)
sorted_T = tuple(sorted(T))

print("Sorted tuple:", sorted_T)



#QUESTION 2
def calculate_sum(n):
    return sum(range(n + 1))
result = int(input("Enter the 'n'th term : "))
test = calculate_sum(result)
print(f"Sum of numbers from 0 to {result} : ", test)
