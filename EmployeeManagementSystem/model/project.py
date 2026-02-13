class Project:
    def __init__(self, project_id, name, client_id):
        self.project_id = project_id
        self.name = name
        self.client_id = client_id
        self.status = "Planned"

    def save(self, db):
        db.execute(
            "INSERT INTO project VALUES (%s,%s,%s,%s)",
            (self.project_id, self.name, self.status, self.client_id)
        )
