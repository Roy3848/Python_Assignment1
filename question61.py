# get only unique items from dictionary
# Method 1 (To get unique keys in python)
dicti1 = {"name": "Sayak", "Last_name": "Roy", "Address": "Kolkata", "Phone_No": 6378945623, "Company": "Mindbowser",
          "Company": "Infosys",
          "place": "Kolkata"}
print(set(dicti1.keys()))


# Method 1 (To get unique values in python)
print(set(dicti1.values()))

# Method 3 (Using loops)

list1 = []
for values in dicti1.values():
    if values in list1:
        continue
    else:
        list1.append(values)

print(set(list1))


# Method 4 (Using  dictionary comprehensions)

result_final = set(list(value1 for dicti in dicti1 for value1 in dicti1.values()))
print(result_final)
