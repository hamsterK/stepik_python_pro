def convert(text):
    lower_count = len(list(filter(str.islower, text)))
    upper_count = len(list(filter(str.isupper, text)))
    if lower_count >= upper_count:
        return text.lower()
    return text.upper()


print(convert('pyTHON'))

print(convert('pi31415!'))

