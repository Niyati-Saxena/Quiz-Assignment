import sqlite3

class Question:
    def __init__(self, prompt, answer, hint):
        self.prompt = prompt
        self.answer = answer
        self.hint = hint

def create_table():
    conn = sqlite3.connect('quiz.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS leaderboard (name TEXT, score REAL)''')
    conn.commit()
    conn.close()

def save_to_db(name, score):
    conn = sqlite3.connect('quiz.db')
    c = conn.cursor()
    c.execute("INSERT INTO leaderboard (name, score) VALUES (?, ?)", (name, score))
    conn.commit()
    conn.close()

def load_leaderboard():
    conn = sqlite3.connect('quiz.db')
    c = conn.cursor()
    c.execute("SELECT name, score FROM leaderboard ORDER BY score DESC")
    return c.fetchall()

def display_leaderboard():
    leaderboard = load_leaderboard()
    print("\nLeaderboard:")
    for idx, (name, score) in enumerate(leaderboard, start=1):
        print(f"{idx}. {name} - {score} points")

def run_quiz(questions, player_name):
    score = 0
    hint_used = False

    for question in questions:
        print(question.prompt)
        answer = input("Your answer (or type 'e' to use a hint): ")

        if answer.lower() == "e":
            print(f"Hint: {question.hint}")
            answer = input("Your answer: ")
            hint_used = True

        if answer.lower() == question.answer.lower():
            score += 1 if not hint_used else 0.5
        hint_used = False

    print(f"\nYou got {score}/{len(questions)} correct, {player_name}!")
    save_to_db(player_name, score)

if __name__ == "__main__":
    create_table()

    question_prompts = [
        "What is the output of the following code?\n```python\nx = [1, 2, 3, 4]\nprint(x[1:3])\n```\n(a) [1, 2]\n(b) [2, 3]\n(c) [3, 4]\n(d) [1, 2, 3]\n(e) Use Hint\n",
        "Which of the following is a mutable data type in Python?\n(a) Tuple\n(b) String\n(c) List\n(d) Integer\n(e) Use Hint\n",
        "What keyword is used to create a function in Python?\n(a) def\n(b) func\n(c) function\n(d) define\n(e) Use Hint\n",
        "What will be the output of the following code?\n```python\ndef add(a, b):\n    return a + b\n\nresult = add(2, 3)\nprint(result)\n```\n(a) 23\n(b) 5\n(c) [2, 3]\n(d) None\n(e) Use Hint\n",
        "Which of the following statements is true about Python?\n(a) Python is a low-level programming language.\n(b) Python does not support object-oriented programming.\n(c) Python is an interpreted language.\n(d) Python has no built-in data structures.\n(e) Use Hint\n"
    ]

    question_hints = [
        "Remember how Python lists are indexed.",
        "Think about the data structures that allow you to change their content after creation.",
        "Functions are defined with a specific keyword.",
        "Focus on how the add function works.",
        "Consider the basic characteristics and capabilities of Python."
    ]

    questions = [
        Question(question_prompts[0], "b", question_hints[0]),
        Question(question_prompts[1], "c", question_hints[1]),
        Question(question_prompts[2], "a", question_hints[2]),
        Question(question_prompts[3], "b", question_hints[3]),
        Question(question_prompts[4], "c", question_hints[4])
    ]

    player_name = input("Enter your name: ")
    run_quiz(questions, player_name)

    display_leaderboard()
