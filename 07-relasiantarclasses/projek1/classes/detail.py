class Detail:
    def __init__(self, product, qyt):
        self.__product=product
        self.__qyt=qyt
    def get_product(self):
        return self.__product
    def get_qyt(self):
        return self.__qyt
    def get_total(self):
        return (self.__product.get_price()*self.__qyt)