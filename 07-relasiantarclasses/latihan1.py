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

class Detail:
    def __init__(self, product, qyt):
        self.__product=product
        self.__qyt=qyt
    def get_product(self):
        return self.__product
    def get_qyt(self):
        return self.__qyt
    def get_total(self):
        return (self.__product.get_price()*self.qyt)     

class Transaction:
    def __init__(self, no, date, costumer):
        self.__no=no
        self.__date=date
        self.__costumer=costumer
        self.__items=[]
    def get_items(self):
        return self.__items
    def add_items(self, item):
        self.__items.append(item)
        print('Data item berhasil disimpan')
    def show_item(self):
        print('%-5s%-25s%-10s%-10s%s'%('NO', 'Product', 'PRICE', 'QYT', 'TOTAL'))
        print('-------------------------------------------------')
        i=1
        for item in self.__items:
            print('%-5i%-25s%-10i%-10i%i'%(i, item.get_product(), get_name(),
                                           item.get_product().get_price(),item.get_qyt(),item.get_total()))   
            print('----------------------')
            i+=1
    def into(self):
        print('No, Transaksi\t: ', self.__no) 
        print('date\t\t: ', self.__date)
        print('Costumer\t: ', self.__costumer)
        self.show_item()    