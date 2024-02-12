from errors.invalid_params import InvalidParams
import re
from datetime import datetime

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
