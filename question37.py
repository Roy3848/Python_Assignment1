# write a program which accepts a sequence of words separated by white space
# as input to print the words composed of digits only

phrase = input("Type in: ")
phrase_splited = phrase.split(' ')

word_list = []
for i in phrase_splited:
    if i not in word_list:
        word_list.append(i)
    else:
        continue
word_list.sort()
print(word_list, end="")
