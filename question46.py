# write a program to slice list into 3 chunks and reverse each list

sample_list = [11, 45, 8, 23, 14, 12, 78, 45, 89]


def reverse_chunks(numbers_list):
    numbers_list1 = numbers_list[0:3]  # first chuck of 3
    numbers_list2 = numbers_list[3:6]  # second chunk of 3
    numbers_list3 = numbers_list[6:9]  # third chunk of 3
    numbers_list1.reverse()  # first chunk reversed
    numbers_list2.reverse()  # second chunk reversed
    numbers_list3.reverse()  # third chunk reversed
    return numbers_list1, numbers_list2, numbers_list3


print(reverse_chunks(sample_list))
