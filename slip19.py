#QUESTION 1
n=int(input("Enter the number of elements to be inserted: "))
a=[]
for i in range(0,n):
    elem=int(input("Enter element  : "))
    a.append(elem)
avg=sum(a)/n
print("Average of elements in the list",round(avg,2))



#QUESTION 2
n = 4
for i in range(n, 0, -1):
    for j in range(1, i+1):
        print(j, end="    ")
    print()