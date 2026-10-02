class Product:
    #Object Constructor
    def __init__(self, product_id, name, unit_price, quantity_in_stock):
        self.product_id = product_id
        self.name = name
        self.unit_price = unit_price
        self.quantity_in_stock = quantity_in_stock

    def restock(self, qty):
        self.quantity_in_stock += qty

    def sell(self, qty):
        if qty > self.quantity_in_stock:
            raise ValueError("Not enough stock available!")
        self.quantity_in_stock -= qty
        return qty * self.unit_price

    def display_info(self): #Polymorphism for product in the menu
        return f"Product {self.product_id}: {self.name}, Price: {self.unit_price}, Stock: {self.quantity_in_stock}"
    
    def to_dict(self):
        return {
            "name": self.name,
            "expiry_date": self.expiry_date.isoformat()  # convert date
        }