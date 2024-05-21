# hospital.py

from Patient import Patient
from Doctor import Doctor
from Appointment import Appointment

class Hospital:
    def __init__(self):
        self.patients = {}
        self.doctors = {}
        self.appointments = {}

    def add_patient(self, patient):
        self.patients[patient.person_id] = patient
        print(f"Patient {patient.name} added.")

    def add_doctor(self, doctor):
        self.doctors[doctor.person_id] = doctor
        print(f"Doctor {doctor.name} added.")

    def schedule_appointment(self, appointment):
        self.appointments[appointment.appointment_id] = appointment
        print(f"Appointment {appointment.appointment_id} scheduled.")

    def display_all_patients(self):
        print("All Patients:")
        for patient in self.patients.values():
            patient.display_info()

    def display_all_doctors(self):
        print("All Doctors:")
        for doctor in self.doctors.values():
            doctor.display_info()

    def display_all_appointments(self):
        print("All Appointments:")
        for appointment in self.appointments.values():
            appointment.display_info()
