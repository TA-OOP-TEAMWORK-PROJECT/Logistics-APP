from errors.invalid_params import InvalidParams
import re
from datetime import datetime, timedelta

def validate_params_count(params: list[str], count: int):
    if len(params) != count:
        raise ValueError('Missing parametres')

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
    tomorrow_date = datetime.now() + timedelta(days=1)
    tomorrow_date = datetime(year=tomorrow_date.year, month=tomorrow_date.month, day=tomorrow_date.day, hour=6, minute=0)
    return tomorrow_date

# def parse_departure_time():
#     tomorrow_date = datetime.now() + timedelta(days=1)
#     tomorrow_date = datetime(year= tomorrow_date.year, month=tomorrow_date.month, day=tomorrow_date.day, hour=6, minute=0)
#     formatted_datetime = tomorrow_date.strftime("%b %d %H:%M")
#     return formatted_datetime


