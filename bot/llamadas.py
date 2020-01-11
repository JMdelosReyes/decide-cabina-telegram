import requests
from configurations import config
def get_token(credentials):
    headers = {"Content-type": "application/json",
        "Accept": "text/plain"}
    r = requests.post(config.API_DECIDE + "authentication/login/", credentials)
    
    return r
    