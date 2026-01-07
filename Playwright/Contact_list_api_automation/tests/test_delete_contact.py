from services.contact_service import ContactService

def test_delete_contact(api_context, auth_token):
    service = ContactService(api_context, auth_token)

    # Create contact
    payload = {
        "firstName": "Archana",
        "lastName": "Delete",
        "email": "archana_delete@test.com",
        "phone": "5555555555"
    }

    create_resp = service.create_contact(payload)
    contact_id = create_resp.json()["_id"]

    # Delete contact
    delete_resp = service.delete_contact(contact_id)
    assert delete_resp.status == 200

    # Verify deletion
    get_resp = service.get_contact_by_id(contact_id)
    assert get_resp.status == 404
