import urllib3
import json

def request(endpoint, key='', version='v3'):
    headers = {
            'X-Api-Key': key,
    }

    http = urllib3.PoolManager()

    resp = http.request(
            'POST',
            'https://www.nymeria.io/api/{}{}'.format(version, endpoint),
            headers=headers,
    )

    return json.loads(resp.data)

class Client:
    def __init__(self, api_key):
        self.key = api_key

    """
        Check your API Key. If the key is valid, this method returns True.
        False is returned otherwise.
    """
    def check_authentication(self):
        resp = request('/check-authentication', key=self.key)

        if 'status' in resp:
            if resp['status'] == 'success':
                return True

        return False

    def enrich(self, *args):
        print(args)

    def verify(self, email):
        print(email)
