import firebase_admin
from firebase_admin import credentials, firestore

# Initialize Firebase Admin SDK
cred = credentials.Certificate("./cligame-firebase-adminsdk-oju86-c97312a6fb.json")

firebase_admin.initialize_app(cred)
db = firestore.client()
def join_game(game_id, player2_name):
    # Reference to the game document in Firestore
    game_ref = db.collection('games').document(game_id)
    
    # Check if the game exists
    game = game_ref.get()
    
    if game.exists:
        # Directly update player2's name with the new value, regardless of the current value
        game_ref.update({
            'player2.name': player2_name,
            'gameState': 'waiting_for_player2'  # You can update game state if necessary
        })
        print(f"Player 2's name has been updated to {player2_name} in game room {game_id}")
    else:
        print(f"Game room with ID {game_id} does not exist")

# Example usage
join_game("game123", "New_Player2_Name")


# Example usage
join_game("sadasda", "Player2_Name]")
