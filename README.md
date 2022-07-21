# Nymeria

[![PyPI version](https://badge.fury.io/py/nymeria.svg)](https://badge.fury.io/py/nymeria)

The official python package to interact with Nymeria's service.

You can use Nymeria to enrich data with contact information such as email
addresses, phone numbers and social links. The python package wraps Nymeria's [public
API](https://www.nymeria.io/developers) so you don't have to.

![Nymeria makes finding contact details a breeze.](https://www.nymeria.io/assets/images/marquee.png)

## Usage

#### Installation

```bash
$ pip install nymeria
```

#### Setting and Checking an API Key.

```python
from nymeria import api

client = api.Client('YOUR API KEY GOES HERE')

client.check_authentication() # => True | False
```

All actions that interact with the Nymeria service assume an API key has been
set and will fail if a key hasn't been set. A key only needs to be set once and
can be set at the start of your program.

If you want to check a key's validity you can use the check_authentication
function to verify the validity of a key that has been set. If no error is
returned then the API key is valid.

#### Verifying an Email Address

```python
from nymeria import api

client = api.Client('YOUR API KEY GOES HERE')

client.verify('dev@nymeria.io') # => dict (see below)
```

```json
{
  'data': {
    'result': 'catchall',
    'tags': ['has_dns', 'has_dns_mx', 'smtp_connectable', 'accepts_all', 'has_dns']
  },

  'usage': {
    'used': 861,
    'limit': 10000
  }
}
```

You can verify the deliverability of an email address using Nymeria's service.
The response will contain a result and tags.

The result will either be "valid" or "invalid". The tags will give you
additional details regarding the email address. For example, the tags will tell
you if the mail server connection was successful, if the domain's DNS records
are set up to send and receive email, etc.

#### Enriching a Profile

```python
from nymeria import api

client = api.Client('YOUR API KEY GOES HERE')

# Single Enrichment

client.enrich({ 'url': 'linkedin.com/in/wozniaksteve' }) # => dict (see below)

# Bulk Enrichment (pass n-queries to enrich)

client.enrich({ 'email': 'woz@steve.org' }, { 'url': 'github.com/nymeriaio' }) # => dict (see below)
```

#### Single Enrichment Response

```json
{
  "usage": {
    "used": 4,
    "limit": 100
  },
  "data": {
    "bio": {
      "first_name": "Steve",
      "last_name": "Wozniak",
      "title": "Chief Scientist",
      "company": "Sandisk",
      "company_website": "sandisk.com"
    },
    "emails": [
      {
        "type": "professional",
        "name": "steve",
        "domain": "woz.org",
        "address": "steve@woz.org"
      },
      ...
    ],
    "phone_numbers": [
      ...
    ],
    "social": [
      {
        "type": "linkedin",
        "id": "wozniaksteve",
        "url": "https://www.linkedin.com/in/wozniaksteve"
      }
    ]
  }
}
```

#### Bulk Enrichment Response

```json
{
  "usage": {
    "used": 4,
    "limit": 100
  },
  "data": [
    {
      'meta': {
        'email': 'steve@woz.org'
      },
      'result': {
        "bio": {
          "first_name": "Steve",
          "last_name": "Wozniak",
          "title": "Chief Scientist",
          "company": "Sandisk",
          "company_website": "sandisk.com"
        },
        "emails": [
          {
            "type": "professional",
            "name": "steve",
            "domain": "woz.org",
            "address": "steve@woz.org"
          },
          ...
        ],
        "phone_numbers": [
          ...
        ],
        "social": [
          {
            "type": "linkedin",
            "id": "wozniaksteve",
            "url": "https://www.linkedin.com/in/wozniaksteve"
          }
        ]
      }
    },
    {
      'meta': {
        'url': 'github.com/nymeriaio'
      },
      'result': {
        ...
      }
    },
    ...
  ]
}
```

You can enrich one or more profiles using the enrich function. The enrich
function takes a dict, or an array of dicts. The most common dict keys
to use are `url` and `email`.

If you want to enrich an email address you can specify an email and the Nymeria
service will locate the person and return all associated data for them.
Likewise, you can specify a supported url via the url parameter if you prefer
to enrich via a url.

At this time, Nymeria supports look ups for the following sites:

1. LinkedIn
1. Facebook
1. Twitter
1. GitHub

Please note, if using LinkedIn urls provide the public profile LinkedIn url.

Two other common parameters are filter and require. If you wish to filter out
professional emails (only receive personal emails) you can do so by specifying
"professional-emails" as the filter parameter.

The require parameter works by requiring certain kinds of data. For example,
you can request an enrichment but only receive a result if the profile
contains a phone number (or an email, personal email, professional email,
etc). The following are all valid requirements:

1. "email"
1. "phone"
1. "professional-email"
1. "personal-email"

You can specify multiple requirements by using a comma
between each requirement. For example you can require a
phone and personal email with: "phone,personal-email" as
the require parameter.

#### Searching for People

```python
from nymeria import api

client = api.Client('YOUR API KEY GOES HERE')

# Query for people. Returns previews for each person.
previews = client.people({ 'q': 'Ruby on Rails' }) # => dict (see above)

# Given a person's uuid, unlock their details (including contact info).
people = client.reveal([ r['uuid'] for r in previews['data'] ])

print(people)
```

You can perform searches using Nymeria's database of people. The search works
using two functions:

1. `people` which performs a search and returns a preview of each person.
1. `reveal` which takes uuids of people and returns complete profiles.

Note, using people does not consume any credits but using reveal will
consume credit for each profile that is revealed.

The dict parameter enables you to specify your search criteria. In
particular, you can specify:

1. `q` for general keyword matching text.
1. `location` to match a specific city or country.
1. `company` to match a current company.
1. `title` to match current titles.
1. `has_email` if you only want to find people that have email addresses.
1. `has_phone` if you only want to find people that has phone numbers.
1. `skills` if you are looking to match specific skills.

By default, 10 people will be returned for each page of search
results. You can specify the page as part of your dict if you
want to access additional pages of people.

You can filter the search results and if you want to reveal the
complete details you can do so by sending the uuids via reveal.
Please note, credit will be consumed for each person that is
revealed.

## License

MIT License

Copyright (c) 2022, Nymeria LLC.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
