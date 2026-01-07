from services.contact_service import ContactService

def test_create_contact(api_context, auth_token):
    service = ContactService(api_context, auth_token)

    payload = {
        "firstName": "Archana",
        "lastName": "Malakhed",
        "email": "archana@test.com",
        "phone": "9999999999"
    }

    response = service.create_contact(payload)

    assert response.status == 201
    assert response.json()["firstName"] == "Archana"
