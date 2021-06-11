from classes.customers import Customer
import csv, os.path

#Holds the Customer files in a list and handles file I/O
class CustomerData:
    def __init__(self, source_file):
        #Initialize data using the filename (subdirectory is hard-coded)
        try:
            self.customers = self.populate_customers(source_file)
            # print("I got the customers.")
        except Exception as e:
            print("Inventory retrieval failed, error", e)
            self.customers = []

    def __str__(self):
        #Print a list of all customers with print(self)
        output = ""
        for i, c in enumerate(self.customers):
            output += str(c)
            if i != len(self.customers)-1:
                output += "\n"
        return output
        
    @classmethod
    def populate_customers(cls, source_file):
        #Initializes the Customer list
        cust = []
        my_path = os.path.abspath(os.path.dirname(__file__))
        my_path += "/../data"
        path = os.path.join(my_path, source_file)

        with open(path) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                cust.append(Customer(**dict(row)))
        return cust
    
    def get_customer_videos_by_id(self, id):
        #Gets a customer object
        #Returns a string of their videos
        output = ""
        cust = self.get_customer_by_id(id)
        for v in cust.get_videos():
            output += v
            output += "\n"
        return output

    def get_customer_by_id(self, id):
        #Searches through the list of customers for an id match
        #Returns a customer object
        for c in self.customers:
            if str(id) == c.get_id():
                return c
        raise Exception("Couldn't find customer with that ID.")
        
    def add_customer(self, id, first_name, last_name):
        try:
            existing_id = self.get_customer_by_id(id)
        except:
            # ID not found; okay to add to database
            new_cust = Customer(id, first_name, last_name)
            self.customers.append(new_cust)
            print(f"Thank you for joining, {first_name}!")
            return
        raise Exception("Duplicate ID found, couldn't add new customer!")
        