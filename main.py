import re
from datetime import datetime
from fastapi import FastAPI, Request
from pymongo import MongoClient
from typing import Dict

app = FastAPI()
client = MongoClient("mongo", 27017)
db = client["form_templates"]
collection = db["template"]


@app.post('/get_form')
async def get_form(request: Request):
    form_data = dict(request.query_params)
    typed_form = type_fields(form_data)

    query = {"$and": [{"fields." + key: value} for key, value in typed_form.items()]}
    template = collection.find_one(query)

    if template:
        return template.get("name")
    else:
        return typed_form


def type_fields(fields: Dict[str, str]) -> Dict[str, str]:
    field_types = {}

    for field, value in fields.items():

        if is_date(value):
            field_types[field] = "date"
        elif is_phone_number(value):
            field_types[field] = "phone"
        elif is_email(value):
            field_types[field] = "email"
        else:
            field_types[field] = "text"

    return field_types


def is_date(value: str) -> bool:
    date_formats = ["%d.%m.%Y", "%Y-%m-%d"]
    for date_format in date_formats:
        try:
            datetime.strptime(value, date_format)
            return True
        except ValueError:
            pass
    return False


def is_phone_number(value: str) -> bool:
    phone_pattern = re.compile(r'^\+7 \d{3} \d{3} \d{2} \d{2}$')
    return bool(re.match(phone_pattern, value))


def is_email(value: str) -> bool:
    email_pattern = re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
    return bool(re.match(email_pattern, value))
