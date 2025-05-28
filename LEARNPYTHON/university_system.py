#https://github.com/DANIEL-CHRISTIAN-KIZITO/Kizito_Daniel_Junior.git
# Parent Class
class Person:
    def __init__(self, name, age, id_number):
        self.name = name
        self.age = age
        self.id_number = id_number

    def display_info(self):
        print(f"Name       : {self.name}")
        print(f"Age        : {self.age}")
        print(f"ID Number  : {self.id_number}")

# Subclass: Student
class Student(Person):
    def __init__(self, name, age, id_number, major, gpa):
        super().__init__(name, age, id_number)
        self.major = major
        self.gpa = gpa

    def display_info(self):
        super().display_info()
        print(f"Major      : {self.major}")
        print(f"GPA        : {self.gpa}")

# Subclass: Lecturer
class Lecturer(Person):
    def __init__(self, name, age, id_number, department, courses_taught):
        super().__init__(name, age, id_number)
        self.department = department
        self.courses_taught = courses_taught  # List of course names

    def display_info(self):
        super().display_info()
        print(f"Department : {self.department}")
        print("Courses    : " + ", ".join(self.courses_taught))

# Subclass: Staff
class Staff(Person):
    def __init__(self, name, age, id_number, position, salary):
        super().__init__(name, age, id_number)
        self.position = position
        self.salary = salary

    def display_info(self):
        super().display_info()
        print(f"Position   : {self.position}")
        print(f"Salary     : ${self.salary:,.2f}")

# --- Test Cases ---

# Create Student
student1 = Student("Alice Brown", 20, "S123", "Computer Science", 3.85)
print("\n--- Student Info ---")
student1.display_info()

# Create Lecturer
lecturer1 = Lecturer("Dr. John Doe", 45, "L456", "Engineering", ["Thermodynamics", "Fluid Mechanics"])
print("\n--- Lecturer Info ---")
lecturer1.display_info()

# Create Staff
staff1 = Staff("Mary Johnson", 38, "ST789", "Librarian", 42000)
print("\n--- Staff Info ---")
staff1.display_info()
