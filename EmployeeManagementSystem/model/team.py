class Team:
    def __init__(self, team_id, manager_id, project_id):
        self.team_id = team_id
        self.manager_id = manager_id
        self.project_id = project_id

    def save(self, db):
        db.execute(
            "INSERT INTO team VALUES (%s,%s,%s)",
            (self.team_id, self.manager_id, self.project_id)
        )
