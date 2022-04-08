# Write a function to replace a word and write another function to replace an alphabet

# function to replace one word with another
def replace_word():
   input_string = input("Enter a phrase:\n")  # user input of the phrase
   input_word1 = input("Enter the word to be replaced:\n")  # ask user input which word to be replaced
   input_word2 = input("Enter the word that you wan to replace with\n")  # ask the user the word replaced by which word
   updated_string = input_string.replace(input_word1, input_word2)  # replace function to replace the word
   return updated_string

print(replace_word())


# function to replace one letter with another letter
# the functionality is the same as the above
def replace_alphabet():
   input_word = input("Enter a word\n")
   input_alphabet1 = input("Enter the alphabet you want to replace:\n")
   input_alphabet2 = input("Enter the alphabet you want to replace with:\n")
   updated_word = input_word.replace(input_alphabet1, input_alphabet2)
   return updated_word
print(replace_alphabet())
