from flask import Flask, jsonify, request
import psycopg2
import random

app = Flask(__name__)

# Database connection configuration
DB_CONFIG = {
    "dbname": "devops_quiz",
    "user": "postgres",
    "password": "password",
    "host": "localhost",
    "port": 5432
}

# Establish database connection
def get_db_connection():
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        return conn
    except Exception as e:
        print(f"Error connecting to the database: {e}")
        return None

# Initialize the database
def initialize_database():
    init_sql_path = "../database/init.sql"
    try:
        with open(init_sql_path, 'r') as file:
            init_script = file.read()
        
        conn = get_db_connection()
        if conn:
            cursor = conn.cursor()
            cursor.execute(init_script)
            conn.commit()
            cursor.close()
            conn.close()
            print("Database initialized successfully.")
    except Exception as e:
        print(f"Error initializing the database: {e}")

# Initialize user sessions
user_sessions = {}

@app.route('/')
def home():
    return jsonify({"message": "Welcome to the DevOps-All-In-One Quiz API!"})

@app.route('/start/<username>', methods=['POST'])
def start_quiz(username):
    if username in user_sessions:
        return jsonify({"message": f"Welcome back, {username}. Continue your quiz!"})
    user_sessions[username] = {"section": "Linux", "score": 0, "progress": []}
    return jsonify({"message": f"Hi {username}, let's begin the quiz with the Linux section!"})

@app.route('/question/<username>', methods=['GET'])
def get_question(username):
    if username not in user_sessions:
        return jsonify({"error": "Start the quiz first with /start/<username>"}), 400

    session = user_sessions[username]
    section = session["section"]

    # Fetch questions from the database
    conn = get_db_connection()
    if not conn:
        return jsonify({"error": "Unable to connect to the database"}), 500

    cursor = conn.cursor()
    cursor.execute(
        "SELECT id, question, options FROM questions WHERE section = %s AND id NOT IN %s",
        (section, tuple(session["progress"]) or (0,))
    )
    questions = cursor.fetchall()
    cursor.close()
    conn.close()

    if not questions:
        return jsonify({"message": f"You've completed the {section} section. Use /next_section/<username> to proceed."})

    question = random.choice(questions)
    question_dict = {
        "id": question[0],
        "question": question[1],
        "options": question[2]
    }
    return jsonify(question_dict)

@app.route('/answer/<username>', methods=['POST'])
def submit_answer(username):
    if username not in user_sessions:
        return jsonify({"error": "Start the quiz first with /start/<username>"}), 400

    session = user_sessions[username]
    section = session["section"]
    data = request.get_json()
    question_id = data.get("id")
    answer = data.get("answer")

    conn = get_db_connection()
    if not conn:
        return jsonify({"error": "Unable to connect to the database"}), 500

    cursor = conn.cursor()
    cursor.execute("SELECT answer FROM questions WHERE id = %s AND section = %s", (question_id, section))
    correct_answer = cursor.fetchone()
    cursor.close()
    conn.close()

    if not correct_answer:
        return jsonify({"error": "Invalid question ID."}), 400

    session["progress"].append(question_id)
    if correct_answer[0] == answer:
        session["score"] += 1

    return jsonify({"correct": correct_answer[0] == answer, "score": session["score"]})

@app.route('/next_section/<username>', methods=['POST'])
def next_section(username):
    if username not in user_sessions:
        return jsonify({"error": "Start the quiz first with /start/<username>"}), 400

    session = user_sessions[username]
    sections = ["Linux", "Python", "Git", "Jenkins", "Ansible", "Docker", "Kubernetes", "Terraform"]
    current_index = sections.index(session["section"])
    
    if current_index == len(sections) - 1:
        return jsonify({"message": f"Quiz completed! Final Score: {session['score']}"})

    next_section = sections[current_index + 1]
    session["section"] = next_section
    session["progress"] = []
    return jsonify({"message": f"Proceeding to the {next_section} section. Good luck!"})

if __name__ == '__main__':
    initialize_database()
    app.run(debug=True)
