def hide_card(card_number):
    return '*' * 12 + card_number.replace(' ', '')[12:]

card = '3456 9012 5678 1234'

print(hide_card(card))