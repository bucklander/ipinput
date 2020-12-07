import unittest
import requests
import json
from ipinput import routeLookup, openRouteTableFile, Route

def respIsJson():
    #tests the API server is running and returns valid JSON content
    result = requests.get("http://127.0.0.1:8080/route/1.1.1.1")
    try:
        json.loads(result.text)
    except ValueError:
        return False
    return True

class Unit_Testing(unittest.TestCase):
    def test_apiStatusCode(self):
        #tests the API server is running and return valid HTTP responses
        result = requests.get("http://127.0.0.1:8080/route/1.1.1.1")
        self.assertEqual(result.status_code, 200)

    def test_respIsJson(self):
        #tests the API server is running and returns valid JSON content
        result = respIsJson()
        self.assertTrue(result)

    def test_ECMP(self):
        #tests ECMP is working by resulting in two route results
        result = routeLookup("1.1.1.1")
        self.assertEqual(len(result), 2)

    def test_Obj(self):
        #tests the lookup returns our python Route object type(s)
        result = routeLookup("1.1.1.1")
        self.assertTrue(isinstance(result[0], Route))

if __name__ == '__main__':
    unittest.main()
