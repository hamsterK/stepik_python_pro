"""
Функция должна возвращать строку text, предварительно удалив из нее все символы, перечисленные в строке marks.
"""


def remove_marks(text, marks):
    remove_marks.__dict__.setdefault('count', 0)
    for mark in marks:
        text = text.replace(mark, '')
    remove_marks.__dict__['count'] += 1
    return text


text = 'Hi! Will we go together?'

print(remove_marks(text, '!?'))
print(remove_marks.count)
