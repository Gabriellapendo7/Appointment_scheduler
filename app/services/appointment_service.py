class AppointmentService:
    def __init__(self, db):
        self.db = db

    def add_appointment(self, client_id, date, time):
        query = "INSERT INTO appointments (client_id, date, time) VALUES (?, ?, ?)"
        self.db.execute(query, (client_id, date, time))
        self.db.commit()

    def get_all_appointments(self):
        query = "SELECT * FROM appointments"
        result = self.db.execute(query)
        return result.fetchall()
