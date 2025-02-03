import urllib3
import json

USER_AGENT = 'nymeria.py/1.2.0'

def request(endpoint, key='', version='v4', payload=None, method='POST', fields=None):
    headers = {
            'User-Agent': USER_AGENT,
            'X-Api-Key': key,
    }

    if method == 'POST':
        headers['Content-Type'] = 'application/json'

    http = urllib3.PoolManager()

    body = None

    if payload is not None and method == 'POST':
        body = json.dumps(payload).encode('utf-8')

    resp = http.request(
            method,
            'https://www.nymeria.io/api/{}{}'.format(version, endpoint),
            headers=headers,
            body=body,
            fields=fields,
    )

    return json.loads(resp.data)

class Company:
    def __init__(self, api_key):
        self.key = api_key

    def enrich(self, args):
        return request('/company/enrich', key=self.key, method='GET', fields=args)

    def search(self, args):
        return request('/company/search', key=self.key, method='GET', fields=args)

class Email:
    def __init__(self, api_key):
        self.key = api_key

    def verify(self, email):
        return request('/email/verify', key=self.key, method='GET', fields={ 'email': email })

    def bulk_verify(self, args):
        return request('/email/verify/bulk', key=self.key, method='POST', payload={ 'requests': args })

class Person:
    def __init__(self, api_key):
        self.key = api_key

    def enrich(self, args):
        return request('/person/enrich', key=self.key, method='GET', fields=args)

    def bulk_enrich(self, args):
        return request('/person/enrich/bulk', key=self.key, method='POST', payload={ 'requests': args })

    def search(self, args):
        return request('/person/search', key=self.key, method='GET', fields=args)

    def retrieve(self, args):
        return request('/person/retrieve/{0}'.format(args), key=self.key, method='GET', fields={})

    def bulk_retrieve(self, args):
        return request('/person/retrieve/bulk', key=self.key, method='POST', payload={ 'requests': args })

    def preview(self, args):
        return request('/person/enrich/preview', key=self.key, method='GET', fields=args)

class Client:
    def __init__(self, api_key):
        self.company = Company(api_key)
        self.person = Person(api_key)
        self.email = Email(api_key)
