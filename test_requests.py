import json

import requests

url = "http://127.0.0.1:8000/get_form"

user_existing_template = {"email": "test@gmail.com", "phone": "%2B7 987 654 32 10"}
deadline_existing_template = {"deadline": "20.11.2023", "employee": "Ivan Ivanov"}

data_nonexistent_template = {"date": "2023-03-01", "email": "test@gmail.com"}

field_typing = {"email_field": "test@gmail.com", "date_field": "2022-01-01",
                "phone_field": "%2B7 987 654 32 10", "text_field": "Some text"}


def build_query_params(data):
    return "&".join([f"{key}={value}" for key, value in data.items()])


def test_request(data):
    query_params = build_query_params(data)
    full_url = f"{url}?{query_params}"

    print("Request with data:")
    for key, value in data.items():
        print(f"    {key}:{value}")

    response = requests.post(full_url)

    print("Response from server:")
    print(f"{json.dumps(response.json(), indent=4)}")
    print("----------------------------------------")


test_request(user_existing_template)

test_request(deadline_existing_template)

test_request(data_nonexistent_template)

test_request(field_typing)
