import firebase_admin
from firebase_admin import credentials, firestore

# Initialize Firebase Admin SDK
cred = credentials.Certificate("./cligame-firebase-adminsdk-oju86-c97312a6fb.json")
firebase_admin.initialize_app(cred)

# Initialize Firestore
db = firestore.client()

# Data to add to Firestore
data = {
    'name': 'ggg',  # This is the document name
    'description': 'This is a sample document for the collection.',
    'timestamp': firestore.SERVER_TIMESTAMP  # Optional: add a timestamp
}

# Add a document to the 'db' collection
doc_ref = db.collection('DB').document('ggg')
doc_ref.set(data)  # Use set instead of add to specify document ID

print("Document added to Firestore successfully.")

# Function to listen for changes in the document
def listen_for_changes(doc_ref):
    # Define the callback function
    def callback(doc_snapshot, changes, read_time):
        for doc in doc_snapshot:
            # Print the new name value whenever it changes
            print(f"New name: {doc.to_dict().get('name')}")

    # Start listening to changes in the document
    doc_watch = doc_ref.on_snapshot(callback)

    # Keep the listener alive (you might want to adjust this in a real application)
    print("Listening for changes to the document...")
    while True:
        pass  # Keep the script running to listen for changes

# Call the listener function
listen_for_changes(doc_ref)
