# return new set of identical items from two sets
# Method 1 (using intersection method)
set1 = {10, 20, 30, 40, 50, 60}
set2 = {40, 50, 60, 70, 80, 90}
print(set1.intersection(set2))


# Method 2 (Using for loop)

final_result = []  # an empty list
for i in set1:
    for j in set2:
        if i == j:
            final_result.append(i)
print(set(final_result))
