class Appointment:
    def __init__(self, id, client_id, date, time):
        self.id = id
        self.client_id = client_id
        self.date = date
        self.time = time

    def __repr__(self):
        return f"Appointment(id={self.id}, client_id={self.client_id}, date='{self.date}', time='{self.time}')"
