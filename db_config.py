import json
from faker import Faker

fake = Faker()

sample_entities = {
    "companies": [
        {"id": 1, "CEO": fake.name(), "company": fake.company(), "address": fake.address()},
        {"id": 2, "CEO": fake.name(), "company": fake.company(), "address": fake.address()},
        {"id": 3, "CEO": fake.name(), "company": fake.company(), "address": fake.address()},
        {"id": 4, "CEO": fake.name(), "company": fake.company(), "address": fake.address()},
        {"id": 5, "CEO": fake.name(), "company": fake.company(), "address": fake.address()},

    ],
    "employees": [
        {"id": 1, "name": fake.name(), "phone_number": fake.phone_number()},
        {"id": 2, "name": fake.name(), "phone_number": fake.phone_number()},
        {"id": 3, "name": fake.name(), "phone_number": fake.phone_number()},
        {"id": 4, "name": fake.name(), "phone_number": fake.phone_number()},
        {"id": 5, "name": fake.name(), "phone_number": fake.phone_number()},

    ],
    "products": [
        {"id": 1, "name": fake.word(), "price": fake.random_number(3), "category": fake.word()},
        {"id": 2, "name": fake.word(), "price": fake.random_number(3), "category": fake.word()},
        {"id": 3, "name": fake.word(), "price": fake.random_number(3), "category": fake.word()},
        {"id": 4, "name": fake.word(), "price": fake.random_number(3), "category": fake.word()},
        {"id": 5, "name": fake.word(), "price": fake.random_number(3), "category": fake.word()},
    ],
    "projects": [
        {"id": 1, "name": fake.catch_phrase(), "description": fake.text()},
        {"id": 2, "name": fake.catch_phrase(), "description": fake.text()},
        {"id": 3, "name": fake.catch_phrase(), "description": fake.text()},
        {"id": 4, "name": fake.catch_phrase(), "description": fake.text()},
        {"id": 5, "name": fake.catch_phrase(), "description": fake.text()},
    ],
    "clients": [
        {"id": 1, "name": fake.company(), "contact_person": fake.name(), "email": fake.email()},
        {"id": 2, "name": fake.company(), "contact_person": fake.name(), "email": fake.email()},
        {"id": 3, "name": fake.company(), "contact_person": fake.name(), "email": fake.email()},
        {"id": 4, "name": fake.company(), "contact_person": fake.name(), "email": fake.email()},
        {"id": 5, "name": fake.company(), "contact_person": fake.name(), "email": fake.email()},
    ],
}

with open('db.json', 'w') as json_file:
    json.dump(sample_entities, json_file, indent=2)