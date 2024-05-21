print ("Hello")

# main.py

from Patient import Patient
from Doctor import Doctor, Specialist
from Appointment import Appointment, FollowUpAppointment
from Department import Department
from Room import Room

# Create instances
patient = Patient(person_id=1, name="John Doe", age=30, ailment="Flu")
doctor = Doctor(person_id=101, name="Dr. Smith", age=45, specialty="General Practitioner")
specialist = Specialist(person_id=102, name="Dr. Jane Doe", age=50, specialty="Cardiology", subspecialty="Interventional Cardiology", certifications=["Board Certified in Cardiology", "Fellow of the American College of Cardiology"])

appointment = Appointment(appointment_id=1001, patient=patient, doctor=doctor, date="2024-06-01", time="10:00 AM")
follow_up_appointment = FollowUpAppointment(appointment_id=1002, patient=patient, doctor=specialist, date="2024-06-15", time="11:00 AM", follow_up_reason="Review treatment progress")

department = Department(department_id=201, name="Cardiology", head=specialist)
room = Room(room_id=301, type="ICU", capacity=2)

# Display information
print("Patient Info:")
patient.display_info()
print("\nDoctor Info:")
doctor.display_info()
print("\nSpecialist Info:")
specialist.display_info()
print("\nAppointment Info:")
appointment.display_info()
print("\nFollow-Up Appointment Info:")
follow_up_appointment.display_info()
print("\nDepartment Info:")
department.display_info()
print("\nRoom Info:")
room.display_info()

