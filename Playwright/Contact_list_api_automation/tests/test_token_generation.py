def test_token_generation(auth_token):
    print("Generated Token:", auth_token)
    assert auth_token is not None
