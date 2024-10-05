from fire import db
def update_player1_score(game_id, player1_answer, correct_answer):
    # Reference to the game document in Firestore
    game_ref = db.collection('games').document(game_id)
    
    # Check if the game exists
    game = game_ref.get()
    
    if game.exists:
        game_data = game.to_dict()
        
        # Initialize Player 1's score
        player1_score = game_data['player1']['score']
        
        # Check if Player 1's answer is correct
        if player1_answer == correct_answer:
            player1_score += 1  # Increment Player 1's score
            print(f"Player 1's answer is correct! New score: {player1_score}")
        
        # Update Player 1's score in Firestore
        game_ref.update({
            'player1.score': player1_score
        })
        
        print(f"Scores updated for game room {game_id}: Player 1: {player1_score}")
    else:
        print(f"Game room with ID {game_id} does not exist")
update_player1_score(game_id, player1_answer, correct_answer)