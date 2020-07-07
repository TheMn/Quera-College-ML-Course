import hashlib
import re


def is_email_valid(email):
    return re.fullmatch(r'[0-9a-zA-Z-_]+[@][0-9a-zA-Z]+[.][0-9a-zA-Z][0-9a-zA-Z]?[0-9a-zA-Z]?', email) is not None


def hash_password(password):
    return hashlib.md5(password.encode()).hexdigest()


def process_data(data):
    data = filter(lambda pair: is_email_valid(pair[0]), data)
    data = list(map(lambda t: (t[0], hash_password(t[1])), data))
    return data

# test_data = ["mohammad-@ahmad.c", "mohammad@ahmad.", "mohamma-+d@ahmad.c", "mohamm-_ad@ahmad.c"]
# for data in test_data:
#     print("{}: {}".format(data, is_email_valid(data)))
