import unittest
import requests
import json
import sys
print(sys.path)
sys.path.append('../configurations') 
import config
class TestMethods(unittest.TestCase):

    def test_login(self):
        headers = {"Content-type": "application/json",
        "Accept": "text/plain"}

        credentials = {"username": "administrador", "password":"administrador"}
        r = requests.post(config.API_DECIDE + "authentication/login/", credentials)
        self.assertEqual(r.status_code, 200)

    
    def test_votings_user(self):
        headers = {"Content-type": "application/json",
        "Accept": "text/plain"}      
        id=1
        r = requests.get(config.API_DECIDE + "voting/user/?id="+str(id)) 

        self.assertEqual(r.status_code,200)

    def test_vote_invalid_token(self):

        headers = {"Authorization": "Token 7241666026815e02759fde720bb11c40d01edf21"}
        vote = {
                "voting": 1,
                "voter": 1,
                "vote": { "a": "3", "b": "2" }
            }
        r = requests.post(config.API_DECIDE + "store/", json=vote, headers=headers)

        self.assertEqual(r.status_code, 401)

    def test_vote(self):

        headers = {"Authorization": "Token af6d8a0e398dda94bc6039141708af60f284a3c8"}
        vote = {
                "vote": { "a": "3", "b": "2" },
                "voting": 1,
                "voter": 1,
                "token": 'af6d8a0e398dda94bc6039141708af60f284a3c8'
            }
        r = requests.post(config.API_DECIDE + "store/", json=vote, headers = headers)
        self.assertEqual(r.status_code, 200)

if __name__ == '__main__':
    unittest.main()