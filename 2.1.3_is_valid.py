def is_valid(string):
    if 4 <= len(string) <= 6 and string.isdigit():
        return True
    return False

print(is_valid('4983456'))
