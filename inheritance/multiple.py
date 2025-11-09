class family:
    def show_family(self):
        print("Kita adalah keluarga")
class father(family):
    def __init__(self, name =""):
        self.father_name=name
    def show_father(self):
        print("Ayah saya adalah ", self.father_name)
class mother(family):
    def __init__(self, name =""):
        self.mother_name=name
    def show_mother(self):
        print("Ibu saya adalah ", self.mother_name)
class child (father, mother):
    def show_parent(self):
        self.show_father()
        self.show_mother()

son = child()
son.show_family()
son.father_name="Muhammad Shodiq"
son.mother_name="Muttasila"
son.show_parent()

