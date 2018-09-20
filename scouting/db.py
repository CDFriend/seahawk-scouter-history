from flask import g

# TODO: get actual firebase impl going
from scouting.api.mock.firebase import Firebase


def get_firebase():
    if 'firebase' not in g:
        g.firebase = Firebase()
    return g.firebase
