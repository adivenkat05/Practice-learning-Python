class Item:
    def __init__(self):
        print("Hello from __init__!!")

    def total_price(self, x, y):
        return x * y

item1 = Item() # __init__ will be executed as we initalize.
print(Item.total_price(item1, 100, 20))

item2 = Item() # This is known as Instance.
print(Item.total_price(item2, 50, 5))
