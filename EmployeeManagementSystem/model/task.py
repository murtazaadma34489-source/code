class Task:
    def __init__(self, task_id, name, hours, deadline, project_id):
        self.task_id = task_id
        self.name = name
        self.hours = hours
        self.deadline = deadline
        self.project_id = project_id
        self.status = "Pending"
        self.assigned_dev = None

    def assign_developer(self, dev_id):
        self.assigned_dev = dev_id
        self.status = "In Progress"

    def save(self, db):
        db.execute(
            "INSERT INTO task VALUES (%s,%s,%s,%s,%s,%s,%s)",
            (self.task_id, self.name, self.hours,
             self.deadline, self.status,
             self.project_id, self.assigned_dev)
        )
