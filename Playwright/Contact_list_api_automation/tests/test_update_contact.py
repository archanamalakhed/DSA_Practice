from services.contact_service import ContactService

def test_update_contact(api_context, auth_token):
    service = ContactService(api_context, auth_token)

    # Create contact
    payload = {
        "firstName": "Archana",
        "lastName": "Malakhed",
        "email": "archana_update@test.com",
        "phone": "7777777777"
    }

    create_resp = service.create_contact(payload)
    contact_id = create_resp.json()["_id"]

    # Update contact
    updated_payload = {
        "firstName": "Archana",
        "lastName": "Updated",
        "email": "archana_updated@test.com",
        "phone": "6666666666"
    }

    update_resp = service.update_contact(contact_id, updated_payload)

    assert update_resp.status == 200
    assert update_resp.json()["lastName"] == "Updated"
