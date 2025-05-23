import os
import configparser

# Construct the path 
config_path = os.path.join(os.path.dirname(__file__), '..', 'config.ini')

# Load config
config = configparser.ConfigParser()
config.read(config_path)

BASE_URL = config['DEFAULT']['web_base_url']
API_KEY = config['DEFAULT'].get('api_key', '')

# Define common headers
HEADERS = {
    "x-api-key": API_KEY,
    "Content-Type": "application/json"
}

# Define endpoints
ENDPOINTS = {
    "users": f"{BASE_URL}/users"
}