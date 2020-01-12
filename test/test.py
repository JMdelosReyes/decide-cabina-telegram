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

        credentials = {"username": "decide-moltres", "password":"egc-decide-moltres201920"}
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
                "voting": 3,
                "voter": 1,
                "vote": { "a": "3", "b": "2" }
            }
        r = requests.post(config.API_DECIDE + "store/", json=vote, headers=headers)

        self.assertEqual(r.status_code, 401)

    def test_vote(self):

        headers = {"Authorization": "Token 	963edaa37004c7a0cdf5f8d464740e85cbb541d5"}
        vote = {
                "vote": { "a": "3", "b": "2" },
                "voting": 3,
                "voter": 1,
                "token": '	963edaa37004c7a0cdf5f8d464740e85cbb541d5'
            }
        r = requests.post(config.API_DECIDE + "store/", json=vote, headers = headers)
        self.assertEqual(r.status_code, 200)

if __name__ == '__main__':
    unittest.main()