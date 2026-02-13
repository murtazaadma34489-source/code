from model.task import Task

class TaskController:
    def __init__(self, db):
        self.db = db

    def create_and_assign_task(self, tid, name, hours, deadline, pid, dev_id):
        task = Task(tid, name, hours, deadline, pid)
        task.assign_developer(dev_id)
        task.save(self.db)
        print("Task assigned successfully")
