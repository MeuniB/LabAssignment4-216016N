# Department.py

class Department:
    def __init__(self, department_id, name, head):
        self.department_id = department_id
        self.name = name
        self.head = head  # Should be an instance of Doctor

    def display_info(self):
        print(f"Department ID: {self.department_id}")
        print(f"Name: {self.name}")
        print("Head Info:")
        self.head.display_info()
