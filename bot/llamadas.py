import requests
from configurations import config


def get_token(credentials):

    r = requests.post(config.API_DECIDE + "authentication/login/", credentials)

    return r


def get_votings(id):

    r = requests.get(config.API_DECIDE + "voting/user/?id="+str(id))
    return r


def get_user(token):
    data = {'token': token}
    r = requests.post(config.API_DECIDE + "authentication/getuser/", data)
    return r

def save_vote_data(data_dict):
    
    headers = {"Authorization": "Token " + data_dict['token'],
                "Content-Type": "application/json"}
    
    r = requests.post(config.API_DECIDE + "store/", json=data_dict, headers = headers)

    print(r.status_code)
    return r
