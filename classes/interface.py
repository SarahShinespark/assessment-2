from classes.customer_database import CustomerData
from classes.inventory import Inventory

class Interface:

    def __init__(self, save_after_close = True, max_checkouts = 3):
        #Max # of videos a customer can have out
        self.max_checkouts = max_checkouts
        #Import video and customer data to the container objects
        self.my_inventory = Inventory("inventory.csv")
        self.my_customers = CustomerData("customers.csv")
        self.save_after_close = save_after_close

    def rent_video_by_title_and_customer_id(self, title, id):
        #Option 3
        customer = self.my_customers.get_customer_by_id(id)
        if customer.get_num_checkouts() >= self.max_checkouts:
            raise Exception("You've checked out too many videos! Turn one in first!")
        rental = self.my_inventory.get_video_from_title(title)
        #Get exact name (customer input is case-INsensitive)
        title = rental.get_title()
        if rental.get_copies() == 0:
            raise Exception(f"No copies available for {title}!")
        if customer.has_title(title):
            raise Exception(f"You already checked out {title}! If you've lost it, don't just get another one! This is how videos go out of stock, etc etc")
        rental.set_copies( rental.get_copies() - 1)
        customer.add_video(title)
        print(customer)

    def return_video_by_title_and_customer_id(self, title, id):
        #Option 4
        customer = self.my_customers.get_customer_by_id(id)
        rental = self.my_inventory.get_video_from_title(title)
        #Get exact name (customer input is case-INsensitive)
        title = rental.get_title()
        customer.remove_video(title)
        rental.set_copies( rental.get_copies() + 1)
        print(f"{title} has been returned successfully. Thank you!")
        if rental.is_kid_friendly():
            #Easter egg for WALL-E
            print("Hope your kids liked it!")

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
                    #Display all videos
                    print(self.my_inventory)
                elif choice == "2":
                    #Display a customer
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
                    first_name = input("Please enter your first name: ")
                    last_name = input("Please enter your last name: ")
                    self.my_customers.add_customer(first_name, last_name)
                elif choice == "6":
                    #Exit
                    print("Thanks for using Code Platoon Video! Byeeeeeeeee!")
                    break
                else:
                    raise Exception("That wasn't one of the choices uwu")
            except Exception as e:
                print(e)
        #End main loop
        if self.save_after_close:
            try:
                # Save changes to files
                self.my_customers.persist_customers("customers.csv")
                self.my_inventory.persist_inventory("inventory.csv")
            except Exception as e:
                print(e)
        
# i = Interface(save_after_close = False)
# i.run()