from faker import Faker

fake = Faker()

def generate_user_payload():
    first_name = fake.first_name()
    last_name = fake.last_name()
    email = fake.unique.email()
    phone = str(fake.random_number(digits=10, fix_len=True))  # 10-digit numeric
    password = "Password123"

    return {
        "firstName": first_name,
        "lastName": last_name,
        "email": email,
        "phone": phone,
        "password": password
    }

def create_contact_payload(user=None):
    phone_number = str(fake.random_number(digits=10, fix_len=True))  # numeric only
    return {
        "name": fake.name(),
        "email": fake.unique.email(),
        "phone": phone_number,
        "address": fake.address(),
        "description": fake.sentence()
    }

def update_contact_payload(user_payload=None):
    if user_payload is None:
        user_payload = generate_user_payload()
    return {
        "firstName": user_payload["firstName"],
        "lastName": f"{user_payload['lastName']}_Updated",
        "email": f"updated_{user_payload['email']}",
        "phone": user_payload["phone"]
    }
