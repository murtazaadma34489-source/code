class ProjectSchedule:
    def __init__(self, schedule_id, project_id, team_id, on_schedule=True):
        self.schedule_id = schedule_id
        self.project_id = project_id
        self.team_id = team_id
        self.on_schedule = on_schedule

    def save(self, db):
        db.execute(
            "INSERT INTO project_schedule VALUES (%s,%s,%s,%s)",
            (self.schedule_id, self.project_id,
             self.team_id, self.on_schedule)
        )
