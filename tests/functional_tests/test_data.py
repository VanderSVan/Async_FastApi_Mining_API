from random import uniform

users_json = [
    {
        "username": "admin",
        "email": "admin@example.com",
        "phone": "0123456789",
        "role": "admin",
        "id": 1,
        "status": "confirmed",
        "password": "123456789"
    },
    {
        "username": "user_1",
        "email": "user_1@example.com",
        "phone": "147852369",
        "role": "user",
        "id": 2,
        "status": "confirmed",
        "password": "123654789"
    },
    {
        "username": "user_2",
        "email": "user_2@example.com",
        "phone": "1478523690",
        "role": "user",
        "id": 3,
        "status": "unconfirmed",
        "password": "123654789"
    }
]
ore_concentrates_json = [
    {
        "name": "iron",
        "id": 1
    },
    {
        "name": "copper",
        "id": 2
    },
    {
        "name": "aluminum",
        "id": 3
    }
]
ore_concentrates_content_json = [
    {
        "datetime": "2022-10-03T12:00:00",
        "iron_percent": round(uniform(63, 72), 6),
        "silicon_percent": round(uniform(4, 8), 6),
        "aluminum_percent": round(uniform(0.2, 1), 6),
        "calcium_percent": round(uniform(0.1, 0.3), 6),
        "sulfur_percent": round(uniform(0.02, 0.1), 6),
        "ore_concentrate_id": 1,
        "id": 1
    },
    {
        "datetime": "2022-10-10T12:00:00",
        "iron_percent": round(uniform(63, 72), 6),
        "silicon_percent": round(uniform(4, 8), 6),
        "aluminum_percent": round(uniform(0.2, 1), 6),
        "calcium_percent": round(uniform(0.1, 0.3), 6),
        "sulfur_percent": round(uniform(0.02, 0.1), 6),
        "ore_concentrate_id": 1,
        "id": 2
    },
    {
        "datetime": "2022-10-17T12:00:00",
        "iron_percent": round(uniform(63, 72), 6),
        "silicon_percent": round(uniform(4, 8), 6),
        "aluminum_percent": round(uniform(0.2, 1), 6),
        "calcium_percent": round(uniform(0.1, 0.3), 6),
        "sulfur_percent": round(uniform(0.02, 0.1), 6),
        "ore_concentrate_id": 1,
        "id": 3
    },
    {
        "datetime": "2022-10-24T12:00:00",
        "iron_percent": round(uniform(63, 72), 6),
        "silicon_percent": round(uniform(4, 8), 6),
        "aluminum_percent": round(uniform(0.2, 1), 6),
        "calcium_percent": round(uniform(0.1, 0.3), 6),
        "sulfur_percent": round(uniform(0.02, 0.1), 6),
        "ore_concentrate_id": 1,
        "id": 4
    },
    {
        "datetime": "2022-10-31T12:00:00",
        "iron_percent": round(uniform(63, 72), 6),
        "silicon_percent": round(uniform(4, 8), 6),
        "aluminum_percent": round(uniform(0.2, 1), 6),
        "calcium_percent": round(uniform(0.1, 0.3), 6),
        "sulfur_percent": round(uniform(0.02, 0.1), 6),
        "ore_concentrate_id": 1,
        "id": 5
    },
    {
        "datetime": "2022-11-07T12:00:00",
        "iron_percent": round(uniform(63, 72), 6),
        "silicon_percent": round(uniform(4, 8), 6),
        "aluminum_percent": round(uniform(0.2, 1), 6),
        "calcium_percent": round(uniform(0.1, 0.3), 6),
        "sulfur_percent": round(uniform(0.02, 0.1), 6),
        "ore_concentrate_id": 1,
        "id": 6
    },
    {
        "datetime": "2022-11-14T12:00:00",
        "iron_percent": round(uniform(63, 72), 6),
        "silicon_percent": round(uniform(4, 8), 6),
        "aluminum_percent": round(uniform(0.2, 1), 6),
        "calcium_percent": round(uniform(0.1, 0.3), 6),
        "sulfur_percent": round(uniform(0.02, 0.1), 6),
        "ore_concentrate_id": 1,
        "id": 7
    },
    {
        "datetime": "2022-11-21T12:00:00",
        "iron_percent": round(uniform(63, 72), 6),
        "silicon_percent": round(uniform(4, 8), 6),
        "aluminum_percent": round(uniform(0.2, 1), 6),
        "calcium_percent": round(uniform(0.1, 0.3), 6),
        "sulfur_percent": round(uniform(0.02, 0.1), 6),
        "ore_concentrate_id": 1,
        "id": 8
    },
    {
        "datetime": "2022-11-27T12:00:00",
        "iron_percent": round(uniform(63, 72), 6),
        "silicon_percent": round(uniform(4, 8), 6),
        "aluminum_percent": round(uniform(0.2, 1), 6),
        "calcium_percent": round(uniform(0.1, 0.3), 6),
        "sulfur_percent": round(uniform(0.02, 0.1), 6),
        "ore_concentrate_id": 1,
        "id": 9
    },
    {
        "datetime": "2022-12-05T12:00:00",
        "iron_percent": round(uniform(63, 72), 6),
        "silicon_percent": round(uniform(4, 8), 6),
        "aluminum_percent": round(uniform(0.2, 1), 6),
        "calcium_percent": round(uniform(0.1, 0.3), 6),
        "sulfur_percent": round(uniform(0.02, 0.1), 6),
        "ore_concentrate_id": 1,
        "id": 10
    },
    {
        "datetime": "2022-12-12T12:00:00",
        "iron_percent": round(uniform(63, 72), 6),
        "silicon_percent": round(uniform(4, 8), 6),
        "aluminum_percent": round(uniform(0.2, 1), 6),
        "calcium_percent": round(uniform(0.1, 0.3), 6),
        "sulfur_percent": round(uniform(0.02, 0.1), 6),
        "ore_concentrate_id": 1,
        "id": 11
    },
    {
        "datetime": "2022-12-19T12:00:00",
        "iron_percent": round(uniform(63, 72), 6),
        "silicon_percent": round(uniform(4, 8), 6),
        "aluminum_percent": round(uniform(0.2, 1), 6),
        "calcium_percent": round(uniform(0.1, 0.3), 6),
        "sulfur_percent": round(uniform(0.02, 0.1), 6),
        "ore_concentrate_id": 1,
        "id": 12
    },
    {
        "datetime": "2022-12-26T12:00:00",
        "iron_percent": round(uniform(63, 72), 6),
        "silicon_percent": round(uniform(4, 8), 6),
        "aluminum_percent": round(uniform(0.2, 1), 6),
        "calcium_percent": round(uniform(0.1, 0.3), 6),
        "sulfur_percent": round(uniform(0.02, 0.1), 6),
        "ore_concentrate_id": 1,
        "id": 13
    },
]