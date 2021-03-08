"""jwrap -- is a single-file micro-library that implements
JSON wrapper. Its mission is to make interacting with JSON
a little bit easier without writing extra code.

License: Unlicense (See LICENSE for details).
"""

__version__ = '0.3'

import os
import json


def read_file(path_to_file: str):
    """Return the file data from `path_to_file`."""
    with open(path_to_file, 'r') as json_file:
        return json_file.read()

def write_to_file(path_to_file: str, data):
    """Write `data` to file from `path_to_file`."""
    with open(path_to_file, 'w') as json_file:
        return json_file.write(data)

def load_json_from_file(path_to_file: str):
    """Load JSON data from file from `path_to_file` by `json.load()`.
    Previously call `read_file()`.
    """
    return json.loads(read_file(path_to_file))

def dump_json_to_file(path_to_file: str, data):
    """Dump JSON data and write it to file from `path_to_file`.
    `ensure_ascii` option is disabled, indentation is enabled.
    """
    write_to_file(
            path_to_file,
            json.dumps(data, ensure_ascii=False, indent=4)
        )

class Jwrap(object):
    """The Jwrap object provides a JSON file connection and implements
    a number of methods for manipulating data.
    Some of them duplicate the standard functionality of Python dicts
    and they can be easily replaced with equivalents. For example::

    obj.ins('key', 'value')
    # is equivalent to:
    obj.json()['key'] = 'value'
    """

    def __init__(self, path_to_file):
        """Check `path_to_file`, create directory if not exist
        and create file if not exist. If file is empty write empty
        dict into it. Load JSON from file.

        Varisbles:
        `__file`      -- contains path to json file (`path_to_file`).
        `__json_data` -- contains loaded JSON data from `__file`.
        """
        dirname = os.path.dirname(path_to_file)
        if dirname == '' or dirname == '.':
            self.__file = path_to_file
        else:
            try:
                os.makedirs(dirname, exist_ok=True)
                self.__file = path_to_file
            except OSError:
                return 'Error: Cannot create path: {}'.format(dirname)
        if self.__file:
            if not os.path.exists(self.__file) \
               or os.path.getsize(self.__file) == 0:
                write_to_file(self.__file, '{}')
            self.__json_data = load_json_from_file(self.__file)

    def get_file(self) -> str:
        """Return abspath to `__file`."""
        return os.path.abspath(self.__file)

    def json(self) -> dict:
        """Return `__json_data`."""
        return self.__json_data

    def reload(self):
        """Reload JSON data from file."""
        self.__json_data = load_json_from_file(self.__file)

    def commit(self):
        """Write JSON data to file."""
        dump_json_to_file(self.__file, self.__json_data)

    def keys(self) -> list:
        """Return root level key list."""
        return list(self.__json_data.keys())

    def subkeys(self, key: str) -> list:
        """Return list of `key` subkeys."""
        return list(self.__json_data[key].keys())

    def keys_by_value(self, value) -> list:
        """Return list of keys by value `value`"""
        return [key for key, val in self.__json_data.items() if val == value]

    def ins(self, key: str, value):
        """Insert `key` with value `value`."""
        self.__json_data[key] = value

    def inssub(self, key: str, subkey: str, value):
        """Similar to `ins`, but for subset."""
        self.__json_data[key][subkey] = value

    def rem(self, key: str):
        """Remove value from JSON by `key`."""
        del self.__json_data[key]

    def remsub(self, key: str, subkey: str):
        """Similar to `rem`, but for subset.
        Remove value by `subkey` of `key`.
        """
        del self.__json_data[key][subkey]

if __name__ == '__main__':
    pass
