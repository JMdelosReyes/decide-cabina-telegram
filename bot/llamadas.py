import requests
from configurations import config


def get_token(credentials):

    r = requests.post(config.API_DECIDE + "authentication/login/", credentials)

    return r


def get_votings(id):

    r = requests.get(config.API_DECIDE + "voting/user/?id="+str(id))
    return r


def get_user(token):
    data = {'token': token }
    r = requests.post(config.API_DECIDE + "authentication/getuser/",data)
    return r