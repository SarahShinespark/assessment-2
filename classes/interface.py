from classes.customer_database import CustomerData
from classes.inventory import Inventory

class Interface:

    def __init__(self, max_checkouts = 3):
        #Max # of videos a customer can have out
        self.max_checkouts = max_checkouts
        #Import video and customer data to the container objects
        self.my_inventory = Inventory("inventory.csv")
        self.my_customers = CustomerData("customers.csv")

    def rent_video_by_title_and_customer_id(self, title, id):
        customer = self.my_customers.get_customer_by_id(id)
        if customer.get_num_checkouts() >= self.max_checkouts:
            raise Exception("You've checked out too many videos! Turn one in first!")
        rental = self.my_inventory.get_video_from_title(title)
        if rental.get_copies() == 0:
            raise Exception("No copies available for that video!")
        rental.copies_available -= 1
        customer.add_video(rental.get_title())
        print(customer)

    def return_video_by_title_and_customer_id(self, title, id):
        customer = self.my_customers.get_customer_by_id(id)
        rental = self.my_inventory.get_video_from_title(title)
        customer.remove_video(title)
        rental.copies_available += 1
        print(f"{rental.get_title()} has been returned successfully. Thank you!")

    def run(self):
        #Main loop
        while True:
            main_menu = """
Welcome to Code Platoon Video!
1. View video inventory
2. View customer's rented videos
3. Rent video
4. Return video
5. Add new customer
6. Exit
"""
            print(main_menu)
            choice = input("Please enter a selection: ")
            try:
                if choice == "1":
                    print(self.my_inventory)
                elif choice == "2":
                    id_choice = input("Please enter a customer ID: ")
                    print(self.my_customers.get_customer_by_id(id_choice))
                elif choice == "3":
                    #Rent video
                    print("You want to rent something? Sure thing!")
                    title = input("Please enter the video's title: ")
                    id_choice = input("Please enter the customer's id: ")
                    self.rent_video_by_title_and_customer_id(title, id_choice)
                elif choice == "4":
                    #Return video
                    print("You're ready to return something? Of course!")
                    title = input("Please enter the video's title: ")
                    id_choice = input("Please enter the customer's id: ")
                    self.return_video_by_title_and_customer_id(title, id_choice)
                elif choice == "5":
                    #Add new customer
                    print("Are you new here? We can make an account for you.")
                    id_choice = input("Please enter a unique id number: ")
                    first_name = input("Please enter your first name: ")
                    last_name = input("Please enter your last name: ")
                    self.my_customers.add_customer(id_choice, first_name, last_name)
                elif choice == "6":
                    print("Thanks for using Code Platoon Video! Byeeeeeeeee!")
                    break
                else:
                    raise Exception("That wasn't one of the choices uwu")
            except Exception as e:
                print(e)
        #End main loop, this is where I would persist the data
        
