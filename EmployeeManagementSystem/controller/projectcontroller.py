from model.project import Project

class ProjectController:
    def __init__(self, db):
        self.db = db

    def create_project(self, pid, name, client_id):
        project = Project(pid, name, client_id)
        project.save(self.db)
        print("Project created successfully")
