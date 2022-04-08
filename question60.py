# Check if key exists in dictionary and delete that key value from dictionary

dicti = {"name": "Sayak", "Last_name": "Roy", "Address": "Kolkata", "Phone_No": 6378945623}

if "name" in dicti.keys():
    del dicti["name"]
    print(dicti)
else:
    print("This key does not exist in this dictionary.")

# Method 2 (using get method)
dicti1 = {"name": "Sayak", "Last_name": "Roy", "Address": "Kolkata", "Phone_No": 6378945623, "Company": "Mindbowser"}


def delete_keys(argument):
    if argument.get("Company"):
        del argument["Company"]
    print(argument)


delete_keys(dicti1)
