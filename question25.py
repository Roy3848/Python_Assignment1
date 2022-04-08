# use recursive function to repeat a string number of times
# recursive function which takes two parameters, the first one is the number of times to print
# the string and the second one is the string that to be printed
def recurse(times, word):
    if times > 1:
        return [word] + recurse(times-1, word)
    if times == 1:
        return [word]


print(recurse(10, 'Sayak'))


def recurse1(times, word):
    if times > 1:
        recurse1(times-1, word)
        print(word)
    if times == 1:
        print(word)


recurse1(10, "Roy")


