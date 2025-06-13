from daad import dad

class son(dad):
    def factory(self):
        print("green")
    def house(self):
        print("orange")

s=son()
s.factory()
s.house()
s.car()