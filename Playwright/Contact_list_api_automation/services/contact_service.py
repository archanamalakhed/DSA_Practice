class ContactService:

    def __init__(self, api_context, token):
        self.api = api_context
        self.headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json"
        }

    def create_contact(self, payload):
        return self.api.post("/contacts", data=payload, headers=self.headers)

    def get_contacts(self):
        return self.api.get("/contacts", headers=self.headers)

    def get_contact_by_id(self, contact_id):
        return self.api.get(f"/contacts/{contact_id}", headers=self.headers)

    def update_contact(self, contact_id, payload):
        return self.api.put(f"/contacts/{contact_id}", data=payload, headers=self.headers)

    def delete_contact(self, contact_id):
        return self.api.delete(f"/contacts/{contact_id}", headers=self.headers)
