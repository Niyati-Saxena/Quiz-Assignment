import os

class Question:
    def __init__(self, prompt, answer, hint):
        self.prompt = prompt
        self.answer = answer
        self.hint = hint

def load_leaderboard(filename="leaderboard.txt"):
    if os.path.exists(filename):
        with open(filename, "r") as file:
            leaderboard = [line.strip().split(",") for line in file.readlines()]
            return [(name, float(score)) for name, score in leaderboard]
    return []

def save_leaderboard(leaderboard, filename="leaderboard.txt"):
    with open(filename, "w") as file:
        for name, score in leaderboard:
            file.write(f"{name},{score}\n")

def clear_leaderboard(filename="leaderboard.txt"):
    if os.path.exists(filename):
        open(filename, "w").close()
        print("Leaderboard has been cleared.")
    else:
        print("Leaderboard file does not exist.")

def update_leaderboard(leaderboard, player_name, score):
    leaderboard.append((player_name, score))
    leaderboard.sort(key=lambda x: x[1], reverse=True)
    return leaderboard

def display_leaderboard(leaderboard):
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
    return score

if __name__ == "__main__":
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

    leaderboard = load_leaderboard()

    player_name = input("Enter your name: ")
    score = run_quiz(questions, player_name)

    leaderboard = update_leaderboard(leaderboard, player_name, score)
    save_leaderboard(leaderboard)

    display_leaderboard(leaderboard)

    # Uncomment the next line to clear the leaderboard
    # clear_leaderboard()
