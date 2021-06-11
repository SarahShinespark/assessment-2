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
        rental = self.my_inventory.get_video_from_title(title)
        if rental.get_copies() == 0:
            raise Exception("No copies available for that video!")
        customer = self.my_customers.get_customer_by_id(id)
        if customer.get_num_checkouts() >= self.max_checkouts:
            raise Exception("You've checked out too many videos! Turn one in first!")
        rental.copies_available -= 1
        customer.add_video(title)
        print(customer)

    def return_video_by_title_and_customer_id(self, title, id):
        customer = self.my_customers.get_customer_by_id(id)
        rental = self.my_inventory.get_video_from_title(title)
        customer.remove_video(title)
        rental.copies_available += 1
        print(f"{title} has been returned successfully. Thank you!")

    def run(self):
        #Main loop
        while True:
            main_menu = """\
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
            if choice == "6":
                break
        print("Thanks for using Code Platoon Video! Byeeeeeeeee!")

i = Interface()
i.run()
#print(i.my_customers.get_customer_videos_by_id(4))
# i.rent_video_by_title_and_customer_id("Sing", 4)
# i.return_video_by_title_and_customer_id("The Prestige", 4)
