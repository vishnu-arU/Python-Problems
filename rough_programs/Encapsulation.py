class Order:
    def __init__(self,customer_name,items,total_amount,total_discount):
        self.items =items
        self.customer_name =customer_name
        self.__total_amount =total_amount #private
        self.__total_discount =total_discount #private


    def __calculate_final_total(self): #private method
        return self.__total_amount - self.__total_discount



    def _get_admin_view(self):
        return{
            "items":self.items,
            "name":self.customer_name,
            "total_amount":f"{self.__total_amount}",
            "discount_appilied":f"{self.__total_discount}",
            "final":f"{self.__calculate_final_total()}",
        } 
    
    def get_customer_view(self):
        return{
            "items":self.items,
            "name":self.customer_name,
            "final":self.__calculate_final_total(),
        }

order=Order("vishnu",items=["biriyani","chicken curry"],total_amount=120,total_discount=60)



class Adminportel:
    def show_order(self,order):
        return order._get_admin_view() 
    

class Customer:
    def show_order(self,order):
        return order.get_customer_view()


admin=Adminportel()
print("adminview")
print(admin.show_order(order))


Customer=Customer()
print("customer view")
print(Customer.show_order(order=order))