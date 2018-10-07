import json
import uuid
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
            return _Document(name, self._data[name], self)
        else:
            return _Document(name, None, self)

    def get(self):
        """Get all documents in the collection."""
        return [_Document(key, val, self) for key, val in self._data.items()]

    def where(self, field, operator, value):
        documents = self._data.items()
        if operator == "==":
            return [_Document(key, val) for key, val in documents if val[field] == value]
        else:
            raise NotSupported()

    def add(self, doc):
        """Add a document with a randomly-generated ID to the collection."""
        self.document(uuid.uuid1()).set(doc)

    def _set_key_val(self, key, val):
        self._data[key] = val


class _Document:
    def __init__(self, id, data, collection):
        self.id = id
        self._data = data
        self._collection = collection

    def to_dict(self):
        return self._data

    def set(self, data):
        self._data = data
        self._collection._set_key_val(self.id, data)
