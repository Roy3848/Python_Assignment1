# Count occurrence of each element from list
# Method 1 (using count method)
sample_list = [11, 45, 8, 11, 23, 45, 23, 45, 89, 89, 45, 45, 45, 8, 8, 8, 8, 8]

element = int(input("Which element to check: "))
print(sample_list.count(element))

# Method 2 (using counter from collections)

from collections import Counter

element1 = int(input("Which element to check:\n "))
counter = Counter(sample_list)
print(counter)

# Method 3 (using function)

sample_list1 = [11, 45, 8, 11, 23, 45, 23, 45, 89, 89, 45, 45, 45, 8, 8, 8, 8, 8]


def count_repetition(numbers_list):
    count = 0
    n = int(input("Which number to check: "))
    if n in numbers_list:
        for i in numbers_list:
            if i == n:
                count = count + 1
        return count
    else:
        print("The number does not exist.")


print(count_repetition(sample_list1))

