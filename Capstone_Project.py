import json
import jsonpickle
from pathlib import Path
import pprint

class Customer:
    def __init__(self, id: int, name: str, gender: str, phone_number: str, location_city: str, dob: str) -> None:
        self.id = id # primary key for customer table
        self.name = name
        self.gender = gender
        self.phone_number = phone_number
        self.location_city = location_city
        self.dob = dob

def read_customers(file_path: Path | str, customer_data: dict):
    if file_path.is_file():
        save_file = open(file_path, "r", encoding="utf-8")
        try:
            customer_data = json.load(save_file)
            if isinstance(customer_data, dict):
                if not customer_data["customers"]:
                    customer_data = {"customers": [], "lastId": 0}
            else:
                customer_data = {"customers": [], "lastId": 0}
        except:
            customer_data = {"customers": [], "lastId": 0}
        save_file.close()
    print("Customer Data:")
    pprint.pp(customer_data)
    print()

def update_customers(file_path: Path | str, customer_data: dict):
    json_data = jsonpickle.encode(customer_data, indent=4)
    save_file = open(file_path, "w", encoding="utf-8")
    save_file.write(json_data)
    save_file.close()

if __name__ == "__main__":
    file_path = Path("data.json")
    customer_data = {"customers": [], "lastId": 0}
    read_customers(file_path, customer_data)
    # {
    #     "customers": [
    #         {}
    #     ],
    #     "lastId": 0
    # }
    while True:
        print("Available options:")
        print("1. Create new customer")
        print("2. Read customer data")
        print("3. Update customer data")
        print("4. Delete existing customer")
        print("5. Exit application")
        user_input = input("Select option: ")
        try:
            user_input = int(user_input)
        except:
            print("Input must be an integer.")
        
        if user_input == 1:
            print("Selected option: Create new customer")
            # customer_data["customers"]: list[Customer]
            # id = input("Input customer ID: ")
            customer_data["lastId"] += 1
            id = customer_data["lastId"]
            name = input("Input customer name: ")
            gender = input("Input customer gender: ")
            phone_number = input("Input customer phone number: ")
            location_city = input("Input customer city location: ")
            dob = input("Input customer date of birth: ")
            customer_data["customers"].append(Customer(id, name, gender, phone_number, location_city, dob))
            update_customers(file_path, customer_data)
            print("New customer created!\n")
        
        elif user_input == 2:
            print("Selected option: Read customer data")
            read_customers(file_path, customer_data)
        
        elif user_input == 3:
            print("Selected option: Update customer data")
            while True:
                id = input("Input customer ID: ")
                try:
                    id = int(id)
                    break
                except:
                    print("Input must be an integer.")
            index = 0
            found = False
            for customer in customer_data["customers"]:
                if customer.id == id:
                    found = True
                    break
                index += 1
            if found:
                print(f"Customer with ID '{id}' found.")
                customer_data["customers"][index].name = input("Input customer name: ")
                customer_data["customers"][index].gender = input("Input customer gender: ")
                customer_data["customers"][index].phone_number = input("Input customer phone number: ")
                customer_data["customers"][index].location_city = input("Input customer city location: ")
                customer_data["customers"][index].dob = input("Input customer date of birth: ")
                print("Updating customer data...")
                update_customers(file_path, customer_data)
            else:
                print(f"Customer with ID '{id}' not found.")
        
        elif user_input == 4:
            print("Selected option: Delete existing customer")
            while True:
                id = input("Input customer ID: ")
                try:
                    id = int(id)
                    break
                except:
                    print("Input must be an integer.")
            index = 0
            found = False
            for customer in customer_data["customers"]:
                if customer.id == id:
                    found = True
                    break
                index += 1
            if found:
                print(f"Customer with ID '{id}' found.")
                print("Deleting customer data...")
                customer_data["customers"].pop(index)
                update_customers(file_path, customer_data)
            else:
                print(f"Customer with ID '{id}' not found.")
        
        elif user_input == 5:
            print("Selected option: Exit application")
            print("Saving customer data...")
            update_customers(file_path, customer_data)
            print("Exiting application...")
            break
        else:
            print("The option you entered is not valid.")
    
    print("Done!")
