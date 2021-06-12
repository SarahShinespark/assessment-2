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

    def persist_customers(self, source_file):
        #Saves the Customer list to a file
        my_path = os.path.abspath(os.path.dirname(__file__))
        my_path += "/../data"
        path = os.path.join(my_path, source_file)

        with open(path, "w") as csvfile:
            writer = csv.DictWriter(csvfile,fieldnames=Customer.get_headers())
            writer.writeheader()
            for customer in self.customers:
                writer.writerow(customer.__dict__)

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
        
    def add_customer(self, first_name, last_name):
        #Creates a Customer object with a unique generated ID, and adds them to the container

        #Find largest ID in the Customers container
        max_id = 0
        for c in self.customers:
            cur_id = int(c.get_id())
            if cur_id > max_id:
                max_id = cur_id
        #Add 1 to the largest ID to make a unique entry
        id = max_id + 1
        #Hard to remember the program needs <id> to be a string but it displays the same as an integer
        new_cust = Customer(str(id), first_name, last_name)
        self.customers.append(new_cust)
        print(f"Thank you for joining, {first_name} {last_name}! Your ID is {id}. ~DON'T FORGET~")

        