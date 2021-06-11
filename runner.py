from classes.interface import Interface

i = Interface()
#i.run()
test_customers = i.my_customers
print(test_customers)
test_customers.add_customer(10, "Sarah", "Dellheim")
print(test_customers)
# self.my_customers.add_customer(id_choice, first_name, last_name)
