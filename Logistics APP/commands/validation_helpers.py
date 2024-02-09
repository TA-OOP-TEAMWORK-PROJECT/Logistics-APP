from errors.invalid_params import InvalidParams


def validate_params_count(params: list[str], count: int):
    if len(params) != count:
        raise InvalidParams(count)


def try_parse_float(float_string: str):
    try:
        return float(float_string)
    except:
        raise ValueError('Can not turn to float number!')
