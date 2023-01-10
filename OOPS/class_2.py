class Vehicle:  # This is known as Class.
    def __init__(self, name, reg_no):
        self.name = name
        self.reg_no = reg_no

    def print_details(self):
        print(self.name)
        print(self.reg_no)


car1 = Vehicle("Benz", 123456)
print(car1.name)
print(car1.reg_no)

car2 = Vehicle("Tesla", 34569)
Vehicle.print_details(car2)

# Here, car1 and car2 is known as Object.
