import datetime
from product import Product
class PerishableProduct(Product): #Inheritance
    def __init__(self, product_id, name, unit_price, quantity_in_stock, expiry_date):
        super().__init__(product_id, name, unit_price, quantity_in_stock)
        self.expiry_date = expiry_date

    def is_expired(self):
        return datetime.date.today() > self.expiry_date

    def display_info(self): #Polymorphism
        return f"[Perishable] {self.product_id}, {self.name} (Expires: {self.expiry_date}), Price: {self.unit_price} Stock: {self.quantity_in_stock}"