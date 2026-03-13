questions = [
    {"question": "2+2", "answer": "4"},
    {"question": "capital of India", "answer": "Delhi"}
]

def save_score(name, score):
    with open("scoreboard.txt", "a") as file:
        file.write(name + " - " + str(score) + "\n")

def show_scoreboard():
    try:
        with open("scoreboard.txt", "r") as file:
            print("--- SCOREBOARD ---")
            print(file.read())
    except FileNotFoundError:
        print("No scores yet")

def run_quiz():
    name = input("Enter your name: ")
    score = 0

    for q in questions:
        answer = input(q["question"] + " ")
        if answer.lower() == q["answer"].lower():
            print("Correct")
            score += 1
        else:
            print("Wrong")

    print("Final score:", score)
    save_score(name, score)

def main():
    while True:
        print("----- QUIZ APP -----")
        print("1. Take Quiz")
        print("2. View Scoreboard")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            run_quiz()

        elif choice == "2":
            show_scoreboard()

        elif choice == "3":
            print("Exiting program")
            break

        else:
            print("Invalid choice")

main()