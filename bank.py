from abc import ABC, abstractmethod

class Bank(ABC):
    """ An abstract bank class """
    
    @abstractmethod
    def withdraw(self):
        pass
    
    def basicinfo(self):
        print("This is a generic bank")
        return "Generic bank: 0"

class Swiss(Bank):
    """ A specific type of bank than derives from class Bank """

    def __init__(self):
        self.bal = 1000

    def basicinfo(self):
        print("This is the Swiss Bank")
        return "Swiss Bank: " + str(self.bal)

    def withdraw(self, amount):
        if amount <= self.bal:
            print(f"Withdrawn amount: {amount}")
            self.bal -= amount
            print(f"New Balance: {self.bal}")
            return self.bal
        else:
            print("Insufficient funds")
            return self.bal

def main():
    assert issubclass(Bank, ABC), "Bank must derive from class ABC"
    s = Swiss()
    print(s.basicinfo())
    s.withdraw(30)
    s.withdraw(1000)

if __name__ == "__main__":
    main()
