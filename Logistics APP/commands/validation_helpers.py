from errors.invalid_params import InvalidParams
import re
from datetime import datetime, timedelta


def validate_params_count(params: list[str], count: int, cmd_name):
    if len(params) != count:
        raise InvalidParams(count, cmd_name)

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
    departure_time = datetime(tomorrow_date.year, tomorrow_date.month, tomorrow_date.day, 6, 0)
    return departure_time
