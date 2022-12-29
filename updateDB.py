import firebase_admin
from firebase_admin import firestore, credentials, storage
import cv2
from datetime import datetime, timezone
import pathlib


# Application Default credentials are automatically created.
cred = credentials.Certificate('C:/Users/ZCL/RAPA/zcl-aruco-7e2b77e444f0.json')
app = firebase_admin.initialize_app(cred, {'storageBucket': 'zcl-aruco.appspot.com'})
db = firestore.client()

def updateDB(arucoid, imagePath, volume):
    arucoid = str(arucoid)
    print(arucoid)
    print("------------------UpdateDB------------------------")
    # print(imagePath)
    print("------------------UpdateDB------------------------") 
    filepath = imagePath
    bucket = storage.bucket()
    blob = bucket.blob(filepath)
    blob.upload_from_filename(filepath)
    blob.make_public()

    cabinet = db.collection(u'ZCL').document(arucoid)

    cabinet.update({
    u'remainder': str(volume),
    u'img': blob.public_url,
    u'last_update': datetime.now(timezone.utc)

    })


