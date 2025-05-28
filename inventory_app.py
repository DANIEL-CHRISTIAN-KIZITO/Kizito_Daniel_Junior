# https://github.com/DANIEL-CHRISTIAN-KIZITO/Kizito_Daniel_Junior.git
#inventory_app

class Stock:
    def update(self):
        print("Stock updated in central inventory system")

class Warehouse:
    def update(self):
        print("Stock updated in warehouse")

# Store inherits from both Stock and Warehouse
class Store(Stock, Warehouse):
    pass

# MRO demonstration
store = Store()
store.update()  # Will follow MRO: Stock first

print(Store.__mro__)  # View Method Resolution Order
