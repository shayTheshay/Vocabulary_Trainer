import json
from constants import load_vocab
from editing import unit_exist_in_data, list_units

def testing_mode() -> None: 
    print(f"\nTesting Mode")
    
    data = load_vocab()
    print("These are the names of units:")
    list_units()
    unit:str = input("Enter the unit for the testing: ").lower()
    if not unit_exist_in_data(data, unit):
        print(f"The unit {unit} does not exist in data.")
    else:
        number_of_words, false_words = run_test_session(data, unit)
        evaluate_answers(number_of_words, len(false_words))
        show_incorrect_answers_with_meaning(false_words)
    return None


def run_test_session(data:json, unit:str) -> tuple[int, list[str]]:
    false_answers = []
    number_of_words = 0
    for entry in data[unit]:
        print(f"The word is: {entry['word']}")
        print("What is the meaning?")
        answer = input("").strip()
        number_of_words +=1

        if entry['meaning'] != answer:
            false_answers.append((entry['word'], entry['meaning']))
    return number_of_words, false_answers

def evaluate_answers(number_of_words: int, number_false_words: int) -> None:
    number_percentage = (number_of_words - number_false_words) / (number_of_words ) * 100
    number_percentage = round(number_percentage, 2)
    print(f"You have done: {number_percentage}% correct answers")
    if number_percentage >= 85 :
        print("🌟 Excellent! Great job remembering your vocabulary.")
    elif number_percentage >= 60:
        print("👍 Good work! A bit more practice and you'll master it.")
    elif number_percentage >= 30:
        print("🟡 Keep going! You're getting there, but review needed.")
    else: 
        print("❗Needs improvement. Study the words again and try once more.")
    return None

def show_incorrect_answers_with_meaning(false_answers:list[str]):
    print(f"\nShowing answers for wrong answers:")
    for answer in false_answers:
        print(f"- {answer}")
        input("press enter for going forward")
    return None