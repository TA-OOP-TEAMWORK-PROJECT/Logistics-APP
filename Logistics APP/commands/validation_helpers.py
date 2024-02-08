from errors.invalid_params import InvalidParams


def validate_params_count(params: list[str], count: int, cmd_name: str):
    if len(params) != count:
        raise InvalidParams(cmd_name, count)


def try_parse_float(float_string: str, msg: str):
    try:
        return float(float_string)
    except:
        raise ValueError(msg)
