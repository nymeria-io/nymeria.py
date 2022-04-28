class Client:
    def __init__(self, api_key):
        self.key = api_key

    def check_authentication(self):
        True

    def enrich(self, *args):
        print(args)

    def verify(self, email):
        print(email)
