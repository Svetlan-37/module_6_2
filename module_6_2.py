class Vehicle:
    _COLOR_VARIANTS = ['blue', 'red', 'green', 'pink', 'white']      # атрибут класса

    def __init__(self, owner, model, engine_power, color):
        self.owner = owner                                            # aтрибуты объекта
        self.__model = model
        self.__color = color
        self.__engine_power = engine_power

    def set_color(self, new_color):
        if new_color.lower() in self._COLOR_VARIANTS:
            self.__color = new_color
        else:
            print(f'Нельзя сменить цвет на {new_color}')

    def get_model(self):
        return f'Модель: {self.__model}'

    def get_horsepower(self):
        return f'Мощность двигателя: {self.__engine_power}'

    def get_color(self):
        return f'Цвет: {self.__color}'

    def print_info(self):
        print(self.get_model())
        print(self.get_horsepower())
        print(self.get_color())
        print(f'Владелец: {self.owner}')


class Sedan(Vehicle):
    _PASSENGERS_LIMIT = 5

    def __init__(self, owner, model, color, engine_power):
        super().__init__(owner, model, engine_power, color)


vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'yellow', 500)

vehicle1.print_info()
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'
vehicle1.print_info()