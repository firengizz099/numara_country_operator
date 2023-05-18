from fastapi import FastAPI
import phonenumbers
from phonenumbers import geocoder, carrier

app = FastAPI()

@app.get("/phone_info/{phone_number}")
def get_phone_info(phone_number: str):
    try:
        parsed_number = phonenumbers.parse(phone_number, None)
        country = geocoder.description_for_number(parsed_number, "en")
        operator = carrier.name_for_number(parsed_number, "en")
        return {"country": country, "operator": operator}
    except phonenumbers.phonenumberutil.NumberParseException:
        return {"error": "Invalid phone number"}


