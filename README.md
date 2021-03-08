# jwrap

**jwrap** — is a single-file micro-library that implements JSON wrapper. Its mission is to make interacting with JSON a little bit easier without writing extra code.

More information is available in docstrings:

```
>>> import jwrap
>>> help(jwrap)
```

## Installation

```
pip install jwrap
```

## Quickstart

For example, you can write some data to json file by this:

```python
from jwrap import Jwrap

j = Jwrap('myfile.json')
j.json()['mykey'] = 'my value'
# or j.ins('mykey', 'my value')
j.commit()  # write data to file
```