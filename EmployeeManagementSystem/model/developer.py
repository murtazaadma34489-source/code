from model.employee import Employee

class Developer(Employee):
    def __init__(self, emp_id, name, contact, email, skill):
        super().__init__(emp_id, name, contact, email)
        self.skill = skill
        self.available = True

    def get_role(self):
        return "Developer"

    def save(self, db):
        super().save(db)
        db.execute(
            "INSERT INTO developer VALUES (%s,%s,%s)",
            (self.emp_id, self.skill, self.available)
        )



