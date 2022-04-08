# Check if given char is vowel or consonant

vowels = ['a', 'e', 'i', 'o', 'u']  # list of vowels
# list of consonants
consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
characters = input("Enter a char: \n")
if type(characters) == str:
    # if the character in the vowels
    # print they are vowels
    if characters in vowels:
        print("It is a vowel")
    # if they are consonants then print the following
    elif characters in consonants:
        print("It is a consonant")
    else:
        print("It is neither a vowel nor a consonant")


