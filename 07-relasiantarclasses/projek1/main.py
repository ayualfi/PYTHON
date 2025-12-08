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