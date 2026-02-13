from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self, emp_id, name, contact, email):
        self.emp_id = emp_id
        self.name = name
        self.contact = contact
        self.email = email

    @abstractmethod
    def get_role(self):
        pass

    def save(self, db):
        db.execute(
            "INSERT INTO employee VALUES (%s,%s,%s,%s,%s)",
            (self.emp_id, self.name, self.contact, self.email, self.get_role())
        )
