import pyodbc

def get_connection():
    return pyodbc.connect(
        "Driver={ODBC Driver 17 for SQL Server};"
        "Server=DESKTOP-066PT2N\\SQLEXPRESS,1433;"
        "Database=KasiFreshGrocersDB;"
        "Trusted_Connection=yes;"
    )

class Customer:
    def __init__(self, customer_id, name, loyalty_points=0):
        self.customer_id = customer_id
        self.name = name
        self.loyalty_points = loyalty_points

    def save_to_db(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO Customers (CustomerID, FirstName, LastName, LoyaltyTier, SignupDate)
            VALUES (?, ?, ?, ?, GETDATE())
        """, self.customer_id, self.name.split()[0], self.name.split()[-1], "Bronze")
        conn.commit()
        conn.close()

    @staticmethod
    def load_customers_from_db():
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT CustomerID, FirstName, LastName, LoyaltyTier FROM Customers")
        rows = cursor.fetchall()
        customers = [Customer(row.CustomerID, f"{row.FirstName} {row.LastName}") for row in rows]
        conn.close()
        return customers

    @staticmethod
    def view_customers_from_db():
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT CustomerID, FirstName, LastName, LoyaltyTier FROM Customers")
        for row in cursor.fetchall():
            print(f"ID: {row.CustomerID}, Name: {row.FirstName} {row.LastName}, Tier: {row.LoyaltyTier}")
        conn.close()

    @staticmethod
    def find_customer_in_db(cust_id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT CustomerID, FirstName, LastName, LoyaltyTier FROM Customers WHERE CustomerID=?", cust_id)
        row = cursor.fetchone()
        conn.close()
        if row:
            return Customer(row.CustomerID, f"{row.FirstName} {row.LastName}")
        return None

    def update_points_in_db(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("UPDATE Customers SET LoyaltyTier=? WHERE CustomerID=?", self.loyalty_points, self.customer_id)
        conn.commit()
        conn.close()

    def add_points(self, points):
        self.loyalty_points += points

    def redeem_points(self, points):
        if points <= self.loyalty_points:
            self.loyalty_points -= points
        else:
            print("Not enough points to redeem.")
