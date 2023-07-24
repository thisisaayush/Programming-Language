import re

phone_number_pattern = r'^(\+\d{1,3}[-\s]?)?(\(\d{1,4}\)|\d{1,4})?[-\s]?\d{1,4}[-\s]?\d{1,9}$'

def is_valid_phone_number(phone_number):
    return re.match(phone_number_pattern, phone_number)
