class ElementФамилия:
    def __init__(self, name, symbol, number):
        self.__name = name       
        self.__symbol = symbol    
        self.__number = number
    
    @property
    def name(self):
        return self.__name

    @property
    def symbol(self):
        return self.__symbol

    @property
    def number(self):
        return self.__number

    def dump(self):
        """Выводит значения атрибутов объекта на экран."""
        print(f"Название элемента: {self.name}")
        print(f"Символ элемента: {self.symbol}")
        print(f"Порядковый номер: {self.number}")


chlorine = ElementФамилия(name="Хлор", symbol="Cl", number=17)

chlorine.dump()

print("\nДоступ к атрибутам через свойства:")
print(f"Название: {chlorine.name}")
print(f"Символ: {chlorine.symbol}")
print(f"Номер: {chlorine.number}")
