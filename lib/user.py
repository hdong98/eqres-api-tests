import requests
import time
from lib.constants import ENDPOINTS, HEADERS

# This module contains functions to interact with the ReqRes API for user management.
def timed_request(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        response = func(*args, **kwargs)
        elapsed = time.time() - start
        return response, elapsed
    return wrapper

def get_user(user_id):
    url = f"{ENDPOINTS['users']}/{user_id}"
    return requests.get(url, headers=HEADERS)

def get_users(page=1):
    url = f"{ENDPOINTS['users']}"
    return requests.get(url, headers=HEADERS, params={"page": page})

@timed_request
def create_user(data):
    return requests.post(ENDPOINTS['users'], json=data, headers=HEADERS)

def update_user(user_id, data):
    url = f"{ENDPOINTS['users']}/{user_id}"
    return requests.put(url, json=data, headers=HEADERS)

def delete_user(user_id):
    url = f"{ENDPOINTS['users']}/{user_id}"
    return requests.delete(url, headers=HEADERS)