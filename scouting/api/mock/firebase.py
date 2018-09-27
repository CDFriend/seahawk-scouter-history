import json
from pathlib import Path
from google.cloud.exceptions import *

MOCK_DATA_PATH = Path(__file__).parent.joinpath("mock_data_firebase.json")


class NotSupported(BaseException):
    pass


class Client:
    """Dummy firebase client for testing. Mirrors the google-cloud-firebase
    python package API.
    """
    def __init__(self):
        self._data = json.load(open(MOCK_DATA_PATH, 'r'))

    def collection(self, name):
        if name in self._data:
            return _Collection(self._data[name])
        else:
            raise NotFound


class _Collection:
    def __init__(self, data):
        self._data = data

    def document(self, name):
        """Get a document in the collection. Throw an exception if it doesn't
        exist.
        """
        if name in self._data:
            return _Document(name, self._data[name])
        else:
            raise NotFound

    def get(self):
        """Get all documents in the collection."""
        return [_Document(key, val) for key, val in self._data.items()]

    def where(self, field, operator, value):
        documents = self._data.items()
        if operator == "==":
            return [_Document(key, val) for key, val in documents if val[field] == value]
        else:
            raise NotSupported()


class _Document:
    def __init__(self, id, data):
        self.id = id
        self._data = data

    def to_dict(self):
        return self._data
