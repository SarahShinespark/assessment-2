import unittest
from classes.interface import Interface
from classes.customers import Customer

class InterfaceTestCase(unittest.TestCase):
    """Tests for interface.py."""
    #Contains the containers Inventory (of Videos) and CustomerData (of Customers)
    i = Interface(save_after_close = False)
    c = Customer(1, "Sarah", "Dellheim", "Interstellar/The Dark Knight")

    def test_data_not_empty(self):
        #Verify data read from CSVs is not empty
        self.assertNotEqual(len(self.i.my_inventory.videos), 0)
        self.assertNotEqual(len(self.i.my_customers.customers), 0)
        
    def test_get_customer_by_id(self):
        #Retrieves a customer by their ID and checks the name for a match
        self.assertEqual(self.i.my_customers.get_customer_by_id(1).get_full_name(), "Jon Young")

    def test_get_customer_videos_by_id(self):
        #Retrieves a customer by their ID and checks their checked-out-video string for a match
        self.assertEqual(self.i.my_customers.get_customer_by_id(2).current_video_rentals, "Prometheus/Split/Sing")

    def test_customer_remove_and_add_video(self):
        self.c.add_video("Guardians of the Galaxy")
        self.assertEqual(self.c.current_video_rentals, "Interstellar/The Dark Knight/Guardians of the Galaxy")
        self.c.remove_video("The Dark Knight")
        self.assertEqual(self.c.current_video_rentals,"Interstellar/Guardians of the Galaxy")
        
    def test_get_video_from_title(self):
        self.assertEqual(self.i.my_inventory.get_video_from_title("Interstellar").get_title(),"Interstellar")
        

if __name__ == '__main__':
    unittest.main()
