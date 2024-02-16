from errors.invalid_params import InvalidParams
import re
from datetime import datetime, timedelta
from core.application_data import ApplicationData

def validate_params_count(params: list[str], count: int):
    if len(params) != count:
        raise InvalidParams(count)

def try_parse_float(float_string: str):
    try:
        return float(float_string)
    except:
        raise ValueError('Can not turn to float number!')

def parse_custom_datetime(date_str):
    date_str = re.sub(r'(st|nd|rd|th)', '', date_str)
    date_str = date_str.replace('h', '')
    return datetime.strptime(date_str, "%b %d %H:%M")

def parse_departure_time():
    datetime_now = datetime.now()
    tomorrow_date = datetime_now + timedelta(days=1)
    tomorrow_data = datetime(tomorrow_date.month, tomorrow_date.day, 6, 0)
    return tomorrow_data

def find_customer(number):
    a = ApplicationData()
    for customer in a.find_customer(number):
        if customer.phone_number == number:
            return customer
    return None
