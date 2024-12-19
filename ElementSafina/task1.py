class ElementФамилия:
    def __init__(self, name, symbol, number):
        self.name = name        
        self.symbol = symbol    
        self.number = number    

    def __str__(self):
        return f"Элемент: {self.name}, Символ: {self.symbol}, Номер: {self.number}"


chlorine = ElementФамилия(name="Хлор", symbol="Cl", number=17)

print(chlorine)
