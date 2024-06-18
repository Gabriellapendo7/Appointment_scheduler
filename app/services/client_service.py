class ClientService:
    def __init__(self, db):
        self.db = db

    def add_client(self, name, email, phone):
        query = "INSERT INTO clients (name, email, phone) VALUES (?, ?, ?)"
        self.db.execute(query, (name, email, phone))
        self.db.commit()

    def get_client_id_by_email(self, email):
        query = "SELECT id FROM clients WHERE email = ?"
        result = self.db.execute(query, (email,))
        client = result.fetchone()
        return client['id'] if client else None

    def get_all_clients(self):
        query = "SELECT * FROM clients"
        result = self.db.execute(query)
        return result.fetchall()
