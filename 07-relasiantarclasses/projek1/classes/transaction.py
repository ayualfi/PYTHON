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
