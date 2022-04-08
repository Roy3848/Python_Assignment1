# Create a function that takes a string character as ASCII
# and returns each character hexadecimal value as a string
# Method 1 (Using Codecs)
import codecs


def ascii_to_hex(char):
    hexadecimal = codecs.encode(b"char", encoding="hex")
    return hexadecimal


print(ascii_to_hex("SR"))

# Method 2 (Using hex function)

def hex_conversion(char1):
    result = hex(char1)
    return result


print(hex_conversion(23))
