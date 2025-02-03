# Nymeria

[![PyPI version](https://badge.fury.io/py/nymeria.svg)](https://badge.fury.io/py/nymeria)

The official python package to interact with Nymeria's service.

You can use Nymeria to enrich data with contact information such as email
addresses, phone numbers and social links. The python package wraps Nymeria's [public
API](https://www.nymeria.io/developers) so you don't have to.

![Nymeria makes finding contact details a breeze.](https://www.nymeria.io/static/images/marquee.png)

## Usage

#### Installation

```bash
pip install nymeria
```

#### Setting up a Client

```python
from nymeria import api

client = api.Client('YOUR API KEY GOES HERE')
```

All actions that interact with the Nymeria service assume an API key has been
set and will fail if a key hasn't been set. A key only needs to be set once and
can be set at the start of your program.

#### Verifying an Email Address

```python
from nymeria import api

client = api.Client('YOUR API KEY GOES HERE')

client.email.verify('dev@nymeria.io')
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

client.person.enrich({ 'profile': 'linkedin.com/in/wozniaksteve' }) # => dict (see below)

# Bulk Enrichment (pass n-queries to enrich)

people = client.person.bulk_enrich([
    { 'params': { 'email': 'someone@somewhere.com' } }, 
    { 'params': { 'profile': 'github.com/dhh' } },
    { 'params': { 'profile': 'linkedin.com/in/wozniaksteve' } },
])
```

You can enrich one or more profiles using the enrich function. The enrich
function takes a dict, or an array of dicts. The most common dict keys
to use are `profile` and `email`.

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

people = client.person.search({ 
    'company': 'nymeria',
    'title': 'founder', 
    'limit': 1
})
```

The dict parameter enables you to specify your search criteria. In
particular, you can specify:

1. `first_name` 
1. `last_name` 
1. `title` 
1. `company` 
1. `location` 
1. `country` 
1. `industry` 
1. `limit` for the number of results to return.
1. `offset` the offset from the base results..

By default, 10 people will be returned for each page of search
results. You can specify the page as part of your dict if you
want to access additional pages of people.

## License

MIT License

Copyright (c) 2025, Nymeria LLC.

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
