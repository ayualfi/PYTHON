class someone:
    def __init__(self, name="bayi", age=0):
        self.__name=name
        self.__age=age
    def set_name(self,name):
        self.__name=name
    def get_name(self):
        return self.__name
    def set_age(self,age):
        self.__age=age
    def get_age(self):
        return self.__age
    def info(self):
        print(f"Nama= \t {self.__name}")
        print(f"Age= \t {self.__age}")
#implementasi class
orang1=someone()
orang1.set_name("Ayu")
orang1.set_age(20)
orang1.get_name()
orang1.get_age()
print("Nama= ", orang1.get_name())
print("Age= ", orang1.get_age())


