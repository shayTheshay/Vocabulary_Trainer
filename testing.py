import json
from constants import load_vocab
from editing import unit_exist_in_data, list_units

def testing_mode() -> None: 
    print(f"\nTesting Mode")
    
    data = load_vocab()
    print("These are the names of units:")
    list_units()
    unit:str = input("Enter the unit for the testng: ").lower()
    if not unit_exist_in_data(data, unit):
        print(f"The unit {unit} does not exist in data.")
    else:
        number_of_words, false_words = run_test_session(data, unit)
        evaluate_answers(number_of_words, false_words.count)
        show_incorrect_answers_with_meaning(false_words)
    return None


def run_test_session(data:json, unit:str) -> tuple[int, list[str]]:
    false_answers = []
    number_of_words = 0
    for entry in data[unit]:
        print(f"The word is: {entry['word']}")
        answer = input("What is the meaning? ").lower()
        number_of_words +=1

        if entry['meaning'] != answer:
            false_answers.append((entry['word'], entry['meaning']))
    return number_of_words, false_answers

def evaluate_answers(number_of_words: int, number_false_words: int) -> None:
    print("Great Job buddy")
    return None

def show_incorrect_answers_with_meaning(false_answers:list[str]):
    print("BRO")