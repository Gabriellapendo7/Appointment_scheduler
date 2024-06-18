import sys
import os

# Add the project root directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.db.database import Database
from app.models.client_service import ClientService
from app.models.appointment_service import AppointmentService
from app.models.reminder_service import ReminderService

def main():
    db = Database(db_file='appointments.db')

    if db.connection is None:
        print("Failed to connect to the database. Exiting...")
        return

    client_service = ClientService(db)
    appointment_service = AppointmentService(db)
    reminder_service = ReminderService(db)

    # Get user input for client details
    client_name = input("Enter client name: ")
    client_email = input("Enter client email: ")
    client_phone = input("Enter client phone: ")

    client_service.add_client(client_name, client_email, client_phone)
    client_id = client_service.get_client_id_by_email(client_email)

    # Get user input for appointment details
    appointment_date = input("Enter appointment date (YYYY-MM-DD): ")
    appointment_time = input("Enter appointment time (HH:MM:SS): ")

    appointment_service.add_appointment(client_id, appointment_date, appointment_time)

    # Get user input for reminder details
    reminder_date = input("Enter reminder date (YYYY-MM-DD): ")
    reminder_message = input("Enter reminder message: ")

    reminder_service.add_reminder(client_id, reminder_date, reminder_message)

    # Fetch and display all data
    clients = client_service.get_all_clients()
    appointments = appointment_service.get_all_appointments()
    reminders = reminder_service.get_all_reminders()

    print("Clients:", clients)
    print("Appointments:", appointments)
    print("Reminders:", reminders)

    db.close()

if __name__ == '__main__':
    main()
