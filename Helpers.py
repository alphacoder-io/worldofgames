import requests

def is_int(var_to_check):
    return type(var_to_check) is int

def is_positive_int(var_to_check):
    return is_int(var_to_check) and var_to_check > 0

def is_in_range_int(var_to_check, min, max):
    return is_int(var_to_check) and min <= var_to_check <= max

def convert_to_int(var_to_check):
    try:
        new_int = int(var_to_check)
        return new_int
    except ValueError:
        return None

def convert_to_float(var_to_check):
    try:
        new_float = float(var_to_check)
        return new_float
    except ValueError:
        return None

def get_current_USD_to_ILS_rate():
    try:
        # used free api, limited to 100 requests per hour
        url = "https://free.currconv.com/api/v7/convert?q=USD_ILS&compact=ultra&apiKey=567f3b2cbef4967e3011"
        res = requests.get(url)
        data = res.json()
        return float(data["USD_ILS"])
    except:
        return 1.0