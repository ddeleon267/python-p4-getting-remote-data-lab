import requests
import json
import pdb

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        response = requests.get(self.url)
        # pdb.set_trace()
        return response.content

    def load_json(self):
        return json.loads(self.get_response_body())