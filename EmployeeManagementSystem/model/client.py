class Client:
    def __init__(self, client_id, name):
        self.client_id = client_id
        self.name = name

    def save(self, db):
        db.execute(
            "INSERT INTO client VALUES (%s,%s)",
            (self.client_id, self.name)
        )
