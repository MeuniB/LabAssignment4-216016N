# patient.py

from Person import Person

class Patient(Person):
    def __init__(self, person_id, name, age, ailment):
        super().__init__(person_id, name, age)
        self.ailment = ailment

    def display_info(self):
        super().display_info()
        print(f"Ailment: {self.ailment}")
