import requests
import hashlib


# First Function its working
def request_api_data(query_char):
    url = ('https://api.pwnedpasswords.com/range/' + query_char)
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(f'error fetching: {res.status_code}, check Api.')
    return res

# Find the Hexadecimal Format of the password
# def pwned_api_check(password):
#     print(hashlib.sha1(password.encode('utf-8')).hexdigest().upper())
# ---

def pwned_api_check(password):
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    return sha1password

pwned_api_check('123')
