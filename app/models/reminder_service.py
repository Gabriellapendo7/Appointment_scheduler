class ReminderService:
    def __init__(self, db):
        self.db = db

    def add_reminder(self, appointment_id, reminder_date, reminder_message):
        query = "INSERT INTO reminders (appointment_id, date, message) VALUES (?, ?, ?)"
        self.db.execute(query, (appointment_id, reminder_date, reminder_message))
        self.db.commit()

    def get_all_reminders(self):
        query = "SELECT * FROM reminders"
        result = self.db.execute(query)
        return result.fetchall()
