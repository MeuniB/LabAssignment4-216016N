
# Person.py

class Person:
    def __init__(self, person_id, name, age):
        self.person_id = person_id
        self.name = name
        self.age = age

    def display_info(self):
        print(f"ID: {self.person_id}")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")

