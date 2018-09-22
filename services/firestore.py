import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

class FirestoreService:
    def __init__(self):
        # Use the application default credentials
        cred = credentials.Certificate('./env/smash-for-fun-sport-hub-4b109ff3fc4d.json')
        firebase_admin.initialize_app(cred)

        self.db = firestore.client()
  

    def getInfoFromSore(self):
        users_ref = self.db.collection(u'users').where(u'email', u'==', u'glenn.latomme@gmail.com')
        docs = users_ref.get()

        for doc in docs:
            print(u'{} => {}'.format(doc.id, doc.to_dict()))
        return docs

    