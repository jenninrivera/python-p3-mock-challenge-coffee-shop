class Coffee:
    def __init__(self, name):
        self.name = name
        self.order_list = []
        self.customer_list = []
        
    def orders(self):
        return self.order_list
    
    def customers(self):
        return self.customer_list
    
    def num_orders(self):
        pass
    
    def average_price(self):
        pass

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name_parameter):
        if (not hasattr(self, 'name')) and (type(name_parameter) == str) and (len(name_parameter) >= 3):
            self._name = name_parameter
        else:
            print("Error")

class Customer:
    def __init__(self, name):
        self.name = name
        self.order_list = []
        self.coffee_list = []
        
    def orders(self):
        return self.order_list
    
    def coffees(self):
        return self.coffee_list
    
    def create_order(self, coffee, price):
        pass

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name_parameter):
        if (type(name_parameter) == str) and (1 <= len(name_parameter) <= 15):
            self._name = name_parameter
    
class Order:

    all =[]

    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price

        self.coffee.order_list.append(self)
        self.customer.order_list.append(self)

        Order.all.append(self)

        if not (customer in self.coffee.customer_list):
            self.coffee.customer_list.append(customer)

        if not (coffee in self.customer.coffee_list):
            self.customer.coffee_list.append(coffee)

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, price_parameter):
        if (not hasattr(self, 'price')) and type(price_parameter) == float and 1.0 <= price_parameter <= 10.0:
            self._price = price_parameter
        else:
            print("Error")

    @property
    def customer(self):
        return self._customer

    @customer.setter
    def customer(self, customer_parameter):
        if type(customer_parameter) == Customer:
            self._customer = customer_parameter

    @property
    def coffee(self):
        return self._coffee

    @coffee.setter
    def coffee(self, coffee_parameter):
        if type(coffee_parameter) == Coffee:
            self._coffee = coffee_parameter

