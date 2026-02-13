
from model.database import Database

from controller.taskcontroller import TaskController
from controller.projectcontroller import ProjectController
from model.developer import Developer
from model.projectmanager import ProjectManager
from model.client import Client
from model.team import Team
from model.projectschedule import ProjectSchedule

if __name__ == "__main__":
    db = Database()

    # Employees
    dev = Developer("E1", "Alice", "123", "alice@mail.com", "Python")
    pm = ProjectManager("E2", "Bob", "456", "bob@mail.com")
    dev.save(db)
    pm.save(db)

    # Client
    client = Client("C1", "TechCorp")
    client.save(db)

    # Project
    pc = ProjectController(db)
    pc.create_project("P1", "AI Platform", "C1")

    # Team
    team = Team("T1", "E2", "P1")
    team.save(db)

    # Task
    tc = TaskController(db)
    tc.create_and_assign_task("T101", "Build API", 30, "2025-12-01", "P1", "E1")

    # Schedule
    schedule = ProjectSchedule("S1", "P1", "T1", True)
    schedule.save(db)
