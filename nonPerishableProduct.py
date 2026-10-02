from product import Product
class NonPerishableProduct(Product):#Inheritance
    def __init__(self, product_id, name, unit_price, quantity_in_stock, warranty_months):
        super().__init__(product_id, name, unit_price, quantity_in_stock)
        self.warranty_months = warranty_months

    def display_info(self): #Polymorphism overriden
        return f"[Non-Perishable] ID: {self.product_id}, {self.name} (Warranty: {self.warranty_months} months), Price: {self.unit_price}  Stock: {self.quantity_in_stock}"