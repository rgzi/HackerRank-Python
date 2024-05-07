class VendingMachine:
    def __init__(self, num_items, item_price):
        self.num_items = num_items
        self.item_price = item_price
    
    def buy(self, req_items, money):
        self.req_items = req_items
        self.money = money
        if (self.num_items >= self.req_items and req_items*self.item_price <= self.money):
            self.num_items -= self.req_items
            return money - (self.req_items*self.item_price)
        else:
            if (self.num_items < self.req_items):
                return "Not enough items in the machine"
            else:
                return "Not enough coins"
