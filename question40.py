# Write a program to print out the duplicates from the list
# Method 1 (using for loop)
numbers_list = [12, 24, 35, 70, 88, 120, 155, 99, 12, 7, 8, 93, 67, 47, 76, 34, 43, 76, 23, 1, 12, 88, 7, 6, 2]
seen = set()
uniq = []
for i in numbers_list:
    if i not in seen:
        seen.add(i)
        uniq.append(i)

print(uniq)
print(seen)

# Method 2
print("\nUsing List Comprehension")
seen1 = set()
uniq1 = [i for i in numbers_list if i not in seen1 and not seen1.add(i)]
print(uniq1)
print(seen1)

