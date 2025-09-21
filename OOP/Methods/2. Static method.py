# STATIC METHODS
# ------------------------------------------------
# Static methods belong to the *class itself*,
# not to any single object (instance).
# They are best used for general utility functions
# that don't need access to instance-specific (self) 
# or class-wide (cls) data.
#
# Instance methods, on the other hand, *do* depend on self
# and usually operate on instance data.

class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    # INSTANCE METHOD
    def get_info(self):
        return f"{self.name} = {self.position}"
    
    # STATIC METHOD
    @staticmethod
    def is_valid_position(position):            # Doesn't use: self, bc doesn't need object
        valid_positions = ["Manager", "Cashier", "Cook"]
        return position in valid_positions      # True or False
# ------------------------------------------------------------------------- #

# Creating employees (instances)
employee1 = Employee("Eugene", "Manager")
employee2 = Employee("Squidward", "Cashier")
employee3 = Employee("Spongebob", "Cook")

# 1. STATIC METHOD USAGE
# Best practice: call via the *class* itself
print(Employee.is_valid_position("Rocket Scientist"))  # False

# But it also works from an *instance* (though less common):
print(employee1.is_valid_position("Manager"))  # True

# 2. INSTANCE METHOD USAGE
print(employee2.get_info())   # Squidward = Cashier
print(employee3.get_info())   # Spongebob = Cook


# https://www.youtube.com/watch?v=GZYWTm7JoWs&list=PLZPZq0r_RZOOkUQbat8LyQii36cJf2SWT&index=58