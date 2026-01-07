from services.contact_service import ContactService

def test_get_contact_by_id(api_context, auth_token):
    service = ContactService(api_context, auth_token)

    # Create contact first
    payload = {
        "firstName": "Archana",
        "lastName": "Malakhed",
        "email": "archana_get@test.com",
        "phone": "8888888888"
    }

    create_resp = service.create_contact(payload)
    contact_id = create_resp.json()["_id"]

    # Get contact
    get_resp = service.get_contact_by_id(contact_id)

    assert get_resp.status == 200
    assert get_resp.json()["email"] == payload["email"]
