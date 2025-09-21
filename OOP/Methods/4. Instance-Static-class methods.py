# Instance methods = Operate on individual objects (need 'self')
# Class methods    = Operate on the class itself (need 'cls')
# Static methods   = General utilities (no 'self' or 'cls')

class Student:
    # Class-level attributes (shared across all instances)
    count = 0
    total_gpa = 0

    def __init__(self, name, gpa):
        # Instance-level attributes (unique to each object)
        self.name = name
        self.gpa = gpa
        # Update class-level data whenever a student is created
        Student.count += 1
        Student.total_gpa += gpa

    # INSTANCE METHOD: Operates on a single object (needs self)
    def get_info(self):
        return f"{self.name} has a GPA of {self.gpa}"

    # CLASS METHOD: Operates on the whole class (needs cls)
    @classmethod
    def get_count(cls):
        return f"Total # of students: {cls.count}"

    @classmethod
    def get_average_gpa(cls):
        return f"Average GPA: {cls.total_gpa / cls.count:.2f}" if cls.count else "No students yet."

    # STATIC METHOD: Utility function related to the class, but doesn’t touch its data
    @staticmethod
    def is_valid_gpa(gpa):
        return 0.0 <= gpa <= 4.0


# Creating students automatically updates class-level attributes
student1 = Student("Spongebob", 3.2)
student2 = Student("Patrick", 2.0)
student3 = Student("Sandy", 4.0)

# Using instance method (works on an object)
print(student1.get_info())

# Using class methods (work on the class itself)
print(Student.get_count())
print(Student.get_average_gpa())

# Using static method (utility check, no access to self or cls)
print(Student.is_valid_gpa(3.5))
print(Student.is_valid_gpa(4.5))  # False
