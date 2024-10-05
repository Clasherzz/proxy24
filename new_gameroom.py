from gemini import send_gemini_requests 

from firebase_admin import credentials, firestore

# Initialize Firebase Admin SDK
cred = credentials.Certificate("./cligame-firebase-adminsdk-oju86-c97312a6fb.json")
firebase_admin.initialize_app(cred)
send_gemini_requests ()
# Initialize Firestore
db = firestore.client()
def start_game(question_count,topic,player1):
    topic = "Mathematics"  # Set your desired topic
    # questions = generate_questions()  # Generate questions
    timer_duration = 30  # Timer in seconds

    # Create a new game in Firestore
    db.collection('gamesDB').document(game_id).set({
        'player1': {'name': player1, 'score': 0},
        'player2': {'name': "", 'score': 0},
        'currentTurn': 'player1',
        'gameState': 'active',
        # 'questions': questions,
        'currentQuestionIndex': 0,
        'timer': timer_duration,
        'topic': topic
    })
    print(f"Game started with topic: {topic}")
    # start_timer(game_id)  # Start the timer
start_game("sadasda")