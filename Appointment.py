# appointment.py

class Appointment:
    def __init__(self, appointment_id, patient, doctor, date, time):
        self.appointment_id = appointment_id
        self.patient = patient
        self.doctor = doctor
        self.date = date
        self.time = time

    def display_info(self):
        print(f"Appointment ID: {self.appointment_id}")
        print(f"Date: {self.date}, Time: {self.time}")
        print("Patient Info:")
        self.patient.display_info()
        print("Doctor Info:")
        self.doctor.display_info()
