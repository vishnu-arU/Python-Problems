# changeing the code through inheritence

class app1():
    def v1(self):
        print("orders")

class app1_1(app1):
    def v2(self):
        print("products")

    def v1(self): #same as parent class
        print("cart")

a=app1_1()
a.v1()
a.v2()


# here we have used inheritance to modify the code 
# 