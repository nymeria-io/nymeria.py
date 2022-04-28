# Nymeria

The official python package to interact with the Nymeria service and API.

Nymeria makes it easy to enrich data with contact information such as email
addresses, phone numbers and social links. The ruby gem wraps Nymeria's [public
API](https://www.nymeria.io/developers) so you don't have to.

![Nymeria makes finding contact details a breeze.](https://www.nymeria.io/assets/images/marquee.png)

## Usage

#### Installation

```bash
$ pip install nymeria
```

#### Set and Check an API Key.

```python
from nymeria import api

client = api.Client('ny_apikey')

client.check_authentication() # => True | False
```

All API endpoints assume an api key has been set. You should set the api key
early in your program. The key will automatically be added to all future
requests.

#### Verify an Email Address

```python
# TODO
```

#### Enrich a Profile

```python
# TODO
```

The enrich API works on a profile by profile basis. If you need to enrich
multiple profiles at once you can use the bulk enrichment API.

#### Bulk Enrichment

```python
# TODO
```

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
