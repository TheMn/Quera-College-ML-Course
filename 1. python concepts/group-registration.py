import hashlib
import re

def is_email_valid(email):
    return re.search(r"sa?", email) is not None


test_data = ["salam", "sal", "s", "", "sa", "salm"]
for test in test_data:
    print("{}: {}".format(test, is_email_valid(test)))

# def hash_password(password):
#     return hashlib.md5(password.encode()).hexdigest()
#
# def process_data(data):
#     data = filter(lambda pair: is_email_valid(pair[0]), data)
#     data = list(map(lambda t: (t[0], hash_password(t[1])), data))
#     return data