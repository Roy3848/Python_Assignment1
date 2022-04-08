# Create a function that takes a string and returns it back in camelCase.
# camelCasing("Hello World") ➞ "helloWorld"


def camelCase(s1):
    s1 = s1.lower()
    split_str = s1.split()

    s1 = " ".join(split_str)

    i = 0
    camcase = ""
    for i in range(len(s1)):
        if s1[i] == " " and s1[i + 1] != " ":

            camcase += s1[i + 1].upper()

        else:
            if s1[i - 1] == " ":
                continue

            camcase += s1[i]

    return camcase


camel_Case = camelCase('   Hello      World     ')
print(f'Camel Case : {camel_Case}')
