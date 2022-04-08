# Extend nested list by adding sub list with specific list taken from console
# Method 1 (accepting input from the uer)

nested_list = [[1, 2, 3, 4, 5], [1, 3, 5, 7, 9], [2, 4, 6, 8, 10], [11, 12, 13, 14, 15]]

index = int(input('Enter the index of the list at which you want to enter the element: '))
sub_index = int(input("Enter the sub index at which you want to enter the element: "))
element = int(input("Enter the element you want to enter: "))
nested_list[index].insert(sub_index, element)  # this will add element to sub list of the main list
nested_list.insert(index, element)  # this will add element to the main list itself.
print(nested_list)
