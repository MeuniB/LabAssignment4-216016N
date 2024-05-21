# Appointment.py
from Patient import Patient
from Doctor import Doctor

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

class FollowUpAppointment(Appointment):
    def __init__(self, appointment_id, patient, doctor, date, time, follow_up_reason):
        super().__init__(appointment_id, patient, doctor, date, time)
        self.follow_up_reason = follow_up_reason

    def display_info(self):
        super().display_info()
        print(f"Follow-Up Reason: {self.follow_up_reason}")
