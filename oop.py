# class is abstract definition of certain type of objects
# object is an instance of a class
# attribute is a feature of the class or instance
# method is an operation that the class or instance can implement
# parameter is input taken by a method to influence its behavior
# instantiation is process of creating specific object based on abstract class

class HumanBeing(object):
    def __init__(self, firstname, eyecolor):
        self.firstname = firstname
        self.eyecolor = eyecolor
        self.position = 0

    def walk_steps(self, steps):
        self.position += steps


class FinancialInstrument(object):
    author = 'Robel Kidane'

    def __init__(self, symbol, price):
        self.symbol = symbol
        self.price = price


Apple = FinancialInstrument('AAPL', 100)


class FinancialInstrument(FinancialInstrument):
    def get_price(self):
        return self.price

    def set_price(self, price):
        self.price = price


fi = FinancialInstrument('AAPL', 100)


class PortfolioPosition(object):
    def __init__(self, financial_instrument, position_size):
        self.position = financial_instrument
        self.__position_size = position_size

    def get_position_size(self):
        return self.__position_size

    def update_position_size(self, position_size):
        self.__position_size = position_size


class Vector(object):
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z


v = Vector(1, 2, 3)
