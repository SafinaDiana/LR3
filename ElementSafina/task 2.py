class ElementФамилия:
    def __init__(self, name, symbol, number):
        self.name = name        
        self.symbol = symbol    
        self.number = number    

    def dump(self):
        """Выводит значения атрибутов объекта на экран."""
        print(f"Название элемента: {self.name}")
        print(f"Символ элемента: {self.symbol}")
        print(f"Порядковый номер: {self.number}")


chlorine = ElementФамилия(name="Хлор", symbol="Cl", number=17)

chlorine.dump()
