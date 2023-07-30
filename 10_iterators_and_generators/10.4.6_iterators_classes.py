class CardDeck:
    def __init__(self):
        self.cards = [f'{j} {i}' for i in ("пик", "треф", "бубен", "червей") for j in
                        ("2", "3", "4", "5", "6", "7", "8", "9", "10", "валет", "дама", "король", "туз")]
        self.value = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.value += 1
        return self.cards[self.value]
