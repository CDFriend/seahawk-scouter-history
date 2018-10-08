import os
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

from flask import g

FIREBASE_APP_NAME = "seahawk-scouter-client"


def get_firestore():
    if "firestore" not in g:
        if FIREBASE_APP_NAME not in firebase_admin._apps:
            cred = credentials.Certificate(os.environ["FIREBASE_CREDS"])
            firebase_admin.initialize_app(cred, {
                "projectId": "seahawk-scouter"
            }, name=FIREBASE_APP_NAME)

        g.firestore = firestore.client(firebase_admin.get_app(FIREBASE_APP_NAME))

    return g.firestore
