from inventory import Inventory
from customer import Customer
from perishableProduct import PerishableProduct
from nonPerishableProduct import NonPerishableProduct
import datetime

def main():
    inventory = Inventory()
    customers = Customer.load_customers_from_db()  # now loads from SQL

    while True:
        print("\n=== Kasi Fresh Grocers Menu ===")
        print("1. Add stock or customer")
        print("2. View stock or customer")
        print("3. Sell product")
        print("4. Manage loyalty points")
        print("5. Save & exit")
        print("6. Remove product")

        choice = input("Enter choice: ")
        
        if choice == "1":
            print("\n--- Add Options ---")
            print("a. Add stock")
            print("b. Add customer")
            sub_choice = input("Enter choice (a/b): ").lower()

            if sub_choice == "a":
                try:
                    pid = int(input("Enter product ID: "))
                    name = input("Enter product name: ")
                    price = float(input("Enter unit price: "))
                    qty = int(input("Enter quantity: "))
            
                    product_type = input("Is this product perishable? (y/n): ").lower()
            
                    if product_type == "y":
                        exp_date_str = input("Enter expiry date (YYYY-MM-DD): ")
                        exp_date = datetime.datetime.strptime(exp_date_str, "%Y-%m-%d").date()
                        product = PerishableProduct(pid, name, price, qty, exp_date)
                    else:
                        shelf_life = int(input("Enter shelf life (in months): "))
                        product = NonPerishableProduct(pid, name, price, qty, shelf_life)
            
                    inventory.add_product_to_db(product)   # save directly to SQL
                    print(f"{name} added successfully!")
                except Exception as e:
                    print("Error adding product:", e)

            elif sub_choice == "b":
                try:
                    cust_id = int(input("Enter customer ID: "))
                    cust_name = input("Enter customer name: ")
                    new_customer = Customer(cust_id, cust_name)
                    new_customer.save_to_db()              # save directly to SQL
                    customers.append(new_customer)
                    print(f"Customer {cust_name} added successfully!")
                except Exception as e:
                    print("Error adding customer:", e)
            else:
                print("Invalid option.")

        elif choice == "2":
            print("\n--- View Options ---")
            print("a. View stock")
            print("b. View customers")
            sub_choice = input("Enter choice (a/b): ").lower()

            if sub_choice == "a":
                inventory.view_products_from_db()
            elif sub_choice == "b":
                Customer.view_customers_from_db()
            else:
                print("Invalid option.")

        elif choice == "3":
            try:
                pid = int(input("Enter product ID: "))
                qty = int(input("Enter quantity: "))
                product = inventory.find_product_in_db(pid)
                if product:
                    total = product.sell(qty)
                    inventory.update_product_qty_in_db(pid, product.quantity)
                    print(f"Sold {qty} units. Total: R{total}")
                else:
                    print("Product not found.")
            except Exception as e:
                print("Error:", e)

        elif choice == "4":
            cust_id = int(input("Enter customer ID: "))
            customer = Customer.find_customer_in_db(cust_id)
            if customer:
                print("\n--- Loyalty Options ---")
                print("a. Add points")
                print("b. Redeem points")
                sub_choice = input("Enter choice (a/b): ").lower()

                try:
                    if sub_choice == "a":
                        points = int(input("Enter points to add: "))
                        customer.add_points(points)
                        customer.update_points_in_db()
                        print(f"{points} points added. {customer.name} now has {customer.loyalty_points} points.")
                    elif sub_choice == "b":
                        points = int(input("Enter points to redeem: "))
                        customer.redeem_points(points)
                        customer.update_points_in_db()
                        print(f"{customer.name} now has {customer.loyalty_points} points left.")
                    else:
                        print("Invalid option.")
                except Exception as e:
                    print("Error:", e)
            else:
                print("Customer not found.")

        elif choice == "5":
            print("Data saved to SQL Server. Goodbye!")
            break
        
        elif choice == "6":
            try:
                pid = int(input("Enter product ID to remove: "))
                inventory.remove_product_from_db(pid)
                print("Product removed successfully.")
            except Exception as e:
                print("Error removing product:", e)

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
