# Doctor.py
from Person import Person

class Doctor(Person):
    def __init__(self, person_id, name, age, specialty):
        super().__init__(person_id, name, age)
        self.specialty = specialty

    def display_info(self):
        super().display_info()
        print(f"Specialty: {self.specialty}")

class Specialist(Doctor):
    def __init__(self, person_id, name, age, specialty, subspecialty, certifications):
        super().__init__(person_id, name, age, specialty)
        self.subspecialty = subspecialty
        self.certifications = certifications

    def display_info(self):
        super().display_info()
        print(f"Subspecialty: {self.subspecialty}")
        print(f"Certifications: {', '.join(self.certifications)}")
