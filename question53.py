# Remove repetitive elements from the list

mixed_list = [34, "bc", 34, "bc", 12, 23, 45, 34, "bc", 89, 76, 89, 45, 100]
seen = set()
uniq_values = []

for i in mixed_list:
    if i not in seen:
        seen.add(i)
        uniq_values.append(i)

print(uniq_values)


# Using List comprehension
mixed_list1 = [34, "bc", 34, "bc", 12, 23, 45, 34, "bc", 89, 76, 89, 45, 100]
seen1 = set()
result = [i for i in mixed_list if i not in seen1 and not seen1.add(i)]
print(result)
