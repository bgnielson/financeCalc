class stock:
    def __init__(self, name, symbol, lastPrice):
        self.name = name
        self.symbol = symbol
        self.lastPrice = lastPrice

    def printStock(self):
        print(self.symbol)
        print(self.name)
        print(self.lastPrice)

brk = stock("Berkshire Hathaway series C", "brk.c", 4)

brk.printStock()
