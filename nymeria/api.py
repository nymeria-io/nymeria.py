import urllib3
import json

USER_AGENT = 'nymeria.py/1.0.2'

def request(endpoint, key='', version='v3', payload=None):
    headers = {
            'User-Agent': USER_AGENT,
            'Content-Type': 'application/json',
            'X-Api-Key': key,
    }

    http = urllib3.PoolManager()

    body = None

    if payload is not None:
        body = json.dumps(payload).encode('utf-8')

    resp = http.request(
            'POST',
            'https://www.nymeria.io/api/{}{}'.format(version, endpoint),
            headers=headers,
            body=body,
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

    """
        Enrich one or more records. A record can be enriched via a url, email or
        an identifier. If enriching more than one records you can specify custom
        attributes as well.
    """
    def enrich(self, *args):
        if len(args) > 1:
            resp = request('/bulk-enrich', key=self.key, payload={ 'people': args })

            if 'status' in resp and 'data' in resp and 'usage' in resp:
                if resp['status'] == 'success':
                    return { 'data': resp['data'], 'usage': resp['usage'] }

            message = 'An unknown error ocurred'

            if 'developer_message' in resp:
                message = resp['developer_message']

            return { 'status': 'failure', 'message': message }
        else:
            for arg in args:
                resp = request('/enrich', key=self.key, payload=arg)

                if 'status' in resp and 'data' in resp and 'usage' in resp:
                    if resp['status'] == 'success':
                        return { 'data': resp['data'], 'usage': resp['usage'] }

                if 'developer_message' in resp:
                    message = resp['developer_message']

                return { 'status': 'failure', 'message': message }

    """
        Determines the deliverability of an email address.
    """
    def verify(self, email):
        resp = request('/verify', key=self.key, payload={ 'email': email })

        if 'status' in resp and 'data' in resp and 'usage' in resp:
            if resp['status'] == 'success':
                return { 'data': resp['data'], 'usage': resp['usage'] }

        message = 'An unknown error ocurred'

        if 'developer_message' in resp:
            message = resp['developer_message']

        return { 'result': 'unknown', 'tags': [], 'message': message }
