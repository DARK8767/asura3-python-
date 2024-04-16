#QUESTION 1
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# Set difference
difference = set1 - set2
print("Set Difference:", difference)

# Symmetric difference
symmetric_difference = set1 ^ set2
print("Symmetric Difference:", symmetric_difference)


#QUESTION 2
def count_occurrences(tup):
    occurrences = {}
    for item in tup:
        if item in occurrences:
            occurrences[item] += 1
        else:
            occurrences[item] = 1

    for item, count in occurrences.items():
        if count > 2:
            print(f"{item}: {count} occurrences")

my_tuple = (1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5)
count_occurrences(my_tuple)