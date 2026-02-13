
from model.database import Database

from model.developer import Developer
from model.projectmanager import ProjectManager
from model.client import Client
from model.project import Project
from model.task import Task

def main():
    db = Database()

    while True:
        print("""
        ===== EMPLOYEE & TASK MANAGEMENT SYSTEM =====
        1. Add Developer
        2. Add Project Manager
        3. Add Client
        4. Create Project
        5. Assign Task
        6. View Projects
        7. Exit
        """)

        choice = int(input("Enter choice: "))

        if choice == 1:
            eid = input("Employee ID: ")
            name = input("Name: ")
            contact = input("Contact: ")
            email = input("Email: ")
            skill = input("Skill: ")
            dev = Developer(eid, name, contact, email, skill)
            dev.save(db)
            print("Developer added successfully")

        elif choice == 2:
            eid = input("Employee ID: ")
            name = input("Name: ")
            contact = input("Contact: ")
            email = input("Email: ")
            pm = ProjectManager(eid, name, contact, email)
            pm.save(db)
            print("Project Manager added successfully")

        elif choice == 3:
            cid = input("Client ID: ")
            name = input("Client Name: ")
            client = Client(cid, name)
            client.save(db)
            print("Client added successfully")

        elif choice == 4:
            pid = input("Project ID: ")
            name = input("Project Name: ")
            cid = input("Client ID: ")
            project = Project(pid, name, cid)
            project.save(db)
            print("Project created successfully")

        elif choice == 5:
            tid = input("Task ID: ")
            name = input("Task Name: ")
            hours = float(input("Estimated Hours: "))
            deadline = input("Deadline (YYYY-MM-DD): ")
            pid = input("Project ID: ")
            dev_id = input("Developer ID: ")
            task = Task(tid, name, hours, deadline, pid, dev_id)
            task.save(db)
            print("Task assigned successfully")

        elif choice == 6:
            db.execute("SELECT project_id, project_name, status FROM project")
            for row in db.fetchall():
                print(row)

        elif choice == 7:
            print("Exiting system...")
            break

        else:
            print("Invalid choice")
if __name__ == "__main__":
    main()