class Product:
    def __init__(self, id='', name='', price=0, stock=0):
        self.__id=id
        self.__name=name
        self.__price=price
        self.__stock=stock
    def set_id(self, id):
        self.__id=id
    def get_id(self):
        return self.__id
    def set_name(self, name):
        self.__name=name
    def get_name(self):
        return self.__name
    def set_price(self, price):
        self.__price=price
    def get_price(self):
        return self.__price
    def set_stock(self, stock):
        self.__stock=stock
    def get_stock(self):
        return self.__stock