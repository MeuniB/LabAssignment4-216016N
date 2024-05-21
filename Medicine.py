
Creating a class for medicines in the context of a hospital management system can be very useful. This class will encapsulate the attributes and behaviors of medicines. Here's a basic implementation of a Medicine class, along with some attributes and methods that you might find useful.

Medicine Class Implementation
Attributes:

medicine_id: Unique identifier for the medicine.
name: Name of the medicine.
manufacturer: The company or entity that manufactures the medicine.
expiry_date: Expiry date of the medicine.
price: Price of the medicine.
stock: The quantity of medicine available in stock.
Methods:

display_info(): Method to display the details of the medicine.
update_stock(amount): Method to update the stock quantity.
Example Implementation
python
Copy code
# medicine.py

class Medicine:
    def __init__(self, medicine_id, name, manufacturer, expiry_date, price, stock):
        self.medicine_id = medicine_id
        self.name = name
        self.manufacturer = manufacturer
        self.expiry_date = expiry_date
        self.price = price
        self.stock = stock

    def display_info(self):
        print(f"Medicine ID: {self.medicine_id}")
        print(f"Name: {self.name}")
        print(f"Manufacturer: {self.manufacturer}")
        print(f"Expiry Date: {self.expiry_date}")
        print(f"Price: ${self.price:.2f}")
        print(f"Stock: {self.stock} units")

    def update_stock(self, amount):
        self.stock += amount
        print(f"Stock updated. New stock: {self.stock} units")
