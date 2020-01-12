import unittest
import requests
import json
import sys
sys.path.insert(0, '../configurations') 
import config
class TestMethods(unittest.TestCase):

    def test_login(self):
        headers = {"Content-type": "application/json",
        "Accept": "text/plain"}

        credentials = {"username": "test", "password":"test12345"}
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

        headers = {"Authorization": "Token 4d58e64a10afb15d16153cdd9c777123aa3b1c84"}
        vote = {
                "voting": 2,
                "voter": 1,
                "vote": { "a": "3", "b": "2" }
            }
        r = requests.post(config.API_DECIDE + "store/", json=vote, headers = headers)
        self.assertEqual(r.status_code, 200)

if __name__ == '__main__':
    unittest.main()