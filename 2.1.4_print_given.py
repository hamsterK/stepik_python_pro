def print_given(*args, **kwargs):
    for i in args:
        print(i, type(i))
    for key, value in sorted(kwargs.items()):
        print(key, value, type(value))

print_given(b=2, d=4, c=3, a=1)

# print_given(1, [1, 2, 3], 'three', two=2)


