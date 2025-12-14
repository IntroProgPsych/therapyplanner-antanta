#import all the modules you need, below this line


#write any functions you need, below this line


#use the main() function for your program, define all other functions above main

def main ():
    #use print statements such as this one, to mark important points in the application, to help you with debugging
    print("Starting application...")

#please do not change the lines below, they are needed for your tests to work properly
#write all your code in the current file, and all your tests in the tests.py file
if __name__ == "__main__":
    main()

# starting point

def interpret_load(total):
    
    if total > 9:
        return "High"
    elif total >= 5:
        return "Moderate"
    else:
        return "Low"


def get_valid_input(question):
    
    while True:
        try:
            value = int(input(question))

            if value < 0 or value > 7:
                print("Error: please enter a number between 0 and 7.")
            else:
                return value

        except ValueError:
            print("Error: please enter a numeric value.")


def build_questions():

    questions = []

    clients = ["first", "second", "third"]
    therapies = [
        "IndividualTherapy",
        "GroupTherapy",
        "FamilyTherapy",
        "CoupleTherapy",
        "OnlineTherapy"
    ]

    for client in clients:
        for therapy in therapies:
            questions.append({
                "text": "How many " + therapy.replace("Therapy", " Therapy")
                        + " sessions per week do you have with the "
                        + client + " client?",
                "therapy": therapy
            })

    return questions


def run_quiz():
    questions = build_questions()

    totals = {
        "IndividualTherapy": 0,
        "GroupTherapy": 0,
        "FamilyTherapy": 0,
        "CoupleTherapy": 0,
        "OnlineTherapy": 0
    }

    print("\n--- ♡˚˖𓍢ִ໋❀ Therapy Planner Quiz ˚˖𓍢ִ໋❀♡ ---\n")

    for item in questions:
        answer = get_valid_input(item["text"] + " ")

        if item["therapy"] == "IndividualTherapy":
            totals["IndividualTherapy"] += answer
        elif item["therapy"] == "GroupTherapy":
            totals["GroupTherapy"] += answer
        elif item["therapy"] == "FamilyTherapy":
            totals["FamilyTherapy"] += answer
        elif item["therapy"] == "CoupleTherapy":
            totals["CoupleTherapy"] += answer
        elif item["therapy"] == "OnlineTherapy":
            totals["OnlineTherapy"] += answer

    print("\n--- ˚ʚ♡ɞ˚ Weekly Therapy Load Summary ˚ʚ♡ɞ˚ ---\n")

    for therapy in totals:
        total = totals[therapy]
        result = interpret_load(total)
        print(therapy + ": " + str(total) + " sessions/week → " + result)


if __name__ == "__main__":
    run_quiz()