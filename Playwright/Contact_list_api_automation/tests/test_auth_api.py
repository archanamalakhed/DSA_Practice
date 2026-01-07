def test_user_register_and_login(api_context):
    # Register user
    register_response = api_context.post(
        "/users",
        data={
            "firstName": "Archana",
            "lastName": "Malakhed",
            "email": "auth_test_archana@gmail.com",
            "password": "Password123"
        }
    )

    # Registration can return 201 or 400 (if already exists)
    assert register_response.status in [201, 400]

    # Login user
    login_response = api_context.post(
        "/users/login",
        data={
            "email": "auth_test_archana@gmail.com",
            "password": "Password123"
        }
    )

    assert login_response.status == 200
    assert "token" in login_response.json()
