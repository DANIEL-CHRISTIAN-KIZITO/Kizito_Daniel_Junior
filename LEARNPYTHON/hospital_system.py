# Base class for Hospital Staff
class Staff:
    def report(self):
        print("Staff daily report submitted")

# Doctor class overrides report method
class Doctor(Staff):
    def report(self):
        print("Doctor's report: Checked patients and updated prescriptions")

# Simulated method overloading in Appointment system
class Appointment:
    def book(self, patient_name, time=None):
        if time:
            print(f"Appointment booked for {patient_name} at {time}")
        else:
            print(f"Appointment booked for {patient_name}")

# Test
doc = Doctor()
doc.report()  # Overridden method

appt = Appointment()
appt.book("John Doe")              # Simulated overloading
appt.book("Jane Doe", "2:00 PM")
