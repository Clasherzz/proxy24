def update_player2_score(game_id, player2_answer, correct_answer):
    # Reference to the game document in Firestore
    game_ref = db.collection('gamesDB').document(game_id)
    
    # Check if the game exists
    game = game_ref.get()
    
    if game.exists:
        game_data = game.to_dict()
        
        # Initialize Player 2's score
        player2_score = game_data['player2']['score']
        
        # Check if Player 2's answer is correct
        if player2_answer == correct_answer:
            player2_score += 1  # Increment Player 2's score
            print(f"Player 2's answer is correct! New score: {player2_score}")
        
        # Update Player 2's score in Firestore
        game_ref.update({
            'player2.score': player2_score
        })
        
        print(f"Scores updated for game room {game_id}: Player 2: {player2_score}")
    else:
        print(f"Game room with ID {game_id} does not exist")