import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from models.player import Player


class FirestoreService:
    def __init__(self):
        # Use the application default credentials
        cred = credentials.Certificate(
            './env/smash-for-fun-sport-hub-firebase-adminsdk-5m1f8-5c926b1a20.json')
        firebase_admin.initialize_app(cred)

        self.db = firestore.client()

    def initialize_info_from_store(self, user: Player):
        users_ref = self.db.collection(u'users').where(
            u'displayName', u'==', user.get_full_name().replace(',', ''))
            
        docs = users_ref.stream()

        for doc in docs:
            user.id = doc.id
            return
    
    def update_info_to_store(self, user: Player):
        collection = self.db.collection(u'users')
        if (user.id):
            user_ref = collection.document(user.id)
            user_ref.update(user.to_dict())

        else: 
            collection.add(user.to_dict())
