import pyodbc
from product import Product

def get_connection():
    return pyodbc.connect(
        "Driver={ODBC Driver 17 for SQL Server};"
        "Server=DESKTOP-066PT2N\\SQLEXPRESS,1433;"
        "Database=KasiFreshGrocersDB;"
        "Trusted_Connection=yes;"
    )

class Inventory:
    def __init__(self):
        self.products = []

    def add_product_to_db(self, product):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO Products (ProductName, Category, UnitPrice, SupplierID)
            VALUES (?, ?, ?, ?)
        """, product.name, "General", product.price, 1)  # adjust SupplierID logic
        conn.commit()
        conn.close()

    def view_products_from_db(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT ProductID, ProductName, UnitPrice FROM Products")
        for row in cursor.fetchall():
            print(f"ID: {row.ProductID}, Name: {row.ProductName}, Price: {row.UnitPrice}")
        conn.close()

    def find_product_in_db(self, pid):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT ProductID, ProductName, UnitPrice FROM Products WHERE ProductID=?", pid)
        row = cursor.fetchone()
        conn.close()
        if row:
            return Product(row.ProductID, row.ProductName, row.UnitPrice, 0)
        return None

    def update_product_qty_in_db(self, pid, qty):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("UPDATE Products SET Quantity=? WHERE ProductID=?", qty, pid)
        conn.commit()
        conn.close()

    def remove_product_from_db(self, pid):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM Products WHERE ProductID=?", pid)
        conn.commit()
        conn.close()
