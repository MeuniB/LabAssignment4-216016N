print ("Hello")

# main.py

from Patient import Patient
from Doctor import Doctor
from Appointment import Appointment
from Hospital import Hospital

# Create Hospital object
hospital = Hospital()

# Create Patient objects
patient1 = Patient(person_id=1, name="John Doe", age=30, ailment="Flu")
patient2 = Patient(person_id=2, name="Jane Smith", age=25, ailment="Cold")

# Create Doctor objects
doctor1 = Doctor(person_id=101, name="Dr. Smith", age=45, specialty="General Practitioner")
doctor2 = Doctor(person_id=102, name="Dr. Brown", age=50, specialty="Pediatrician")

# Add patients and doctors to the hospital
hospital.add_patient(patient1)
hospital.add_patient(patient2)
hospital.add_doctor(doctor1)
hospital.add_doctor(doctor2)

# Create Appointment objects
appointment1 = Appointment(appointment_id=1001, patient=patient1, doctor=doctor1, date="2024-06-01", time="10:00 AM")
appointment2 = Appointment(appointment_id=1002, patient=patient2, doctor=doctor2, date="2024-06-02", time="11:00 AM")

# Schedule appointments
hospital.schedule_appointment(appointment1)
hospital.schedule_appointment(appointment2)

# Display all patients, doctors, and appointments
hospital.display_all_patients()
hospital.display_all_doctors()
hospital.display_all_appointments()
