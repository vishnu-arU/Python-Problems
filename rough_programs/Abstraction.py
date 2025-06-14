from abc import ABC,abstractmethod

class featured(ABC):
    @abstractmethod
    def login(self):
        pass

    @abstractmethod
    def logout(self):
        pass


class employee(featured):

    def login(self):
        print("i have logged in")

    def logout(self):
        print("i have logged out")

em=employee()
em.login()
em.logout()