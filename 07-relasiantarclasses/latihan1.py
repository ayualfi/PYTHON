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
        return (self.__product.get_price()*self.__qyt)     

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
    def show_items(self):
        print('%-5s%-25s%-10s%-10s%s'%('NO', 'Product', 'PRICE', 'QYT', 'TOTAL'))
        print('-------------------------------------------------')
        i=1
        for item in self.__items:
            print('%-5i%-25s%-10i%-10i%i'%(i, item.get_product(). get_name(),
                                           item.get_product().get_price(),item.get_qyt(),item.get_total()))   
            print('------------------------------')
            i+=1
    def into(self):
        print('No, Transaksi\t: ', self.__no) 
        print('date\t\t: ', self.__date)
        print('Costumer\t: ', self.__costumer)
        self.show_items()   

from classes.product import Product
from classes.detail import Detail
from classes.transaction import Transaction

products = []
transactions = []

def find_product(id):
    found = None
    for product in products:
        if product.get_id()==id:
            found = product
            return found
def add_product():
    products.append(Product(int(input('ID\t: ')), input('Name\t: '),
                            int(input('Price\t: ')), int(input('Stock\t: '))))
    print('New product added successfully')

def show_products():
    print('%-5s%-20s%-10s%-10s'%('ID', 'NAME', 'PRICE', 'STOCK'))
    print('----------------------------------------------------')
    i=0
    for product in products:
        i+=1
        print('%-5i%-20s%-10i%-10i'%(i,product.get_name(), product.get_price(), product.get_stock()))
        print('---------------------------------------------------')

def add_transaction():
    trans=Transaction(input('Nomor\t: '), input('Date\t: '), input('Costumer\t: '))
    while True:
        id=int(input('ID\t: '))
        product=find_product(id)
        if product==None:
            print('Product not found!')
        else:
            print('Name\t: ', product.get_name())
            print('Price\t: ', product.get_price())
            qyt=int(input('Quantity\t: '))
            print('Total\t: ', qyt*product.get_price())
            trans.add_items(Detail(product,qyt))
        if len(trans.get_items())>0:
            transactions.append(trans)
        add = input('Add item? ').lower()
        if add !='y':
            break
def show_transactions():
    for trans in transactions:
        trans.info()
        print('')
while True:
    print('1. Add product')
    print('2. List Product')
    print('3. Add Transaction')
    print('4. Show Transaction')
    print('5. Exit')
    menu=int(input('Selected menu: '))
    if menu == 1:
        add_product()
    elif menu == 2:
        show_products()
    elif menu == 3:
        add_transaction()
    elif menu == 4:
        show_transactions()
    elif menu == 5:
        break
    else:
        print('Your choice was not found')