import json
from lib.get_requester import GetRequester

URL = 'https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json'
JSON_STRING = '[{"name": "Daniel", "occupation": "LG Fridge Salesman"}, {"name": "Joe", "occupation": "WiFi Fixer"}, {"name": "Avi", "occupation": "DJ"}, {"name": "Howard", "occupation": "Mountain Legend"}]'

def test_get_response():
    '''get_response_body function returns response.'''
    requester = GetRequester(URL)
    response = requester.get_response_body()
    
    # Convert the response (bytes) to a string
    response_str = response.decode('utf-8')
    
    assert response_str == JSON_STRING
