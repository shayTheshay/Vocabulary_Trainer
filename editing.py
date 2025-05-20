import json
import os
from constants import json_name


def editing_mode():
    print(f"\nEditing Mode")
    if json_exist() == False :
        create_json_file()
    term = input(f"1 for adding a word\n2 for deleting a word\n3 update a word\n4 to list words\nEnter: ")
    unit:str = input("Enter the unit: ").lower()

    match term:
        case "1":
            word = input("Enter the word you want to add: ").lower()
            meaning = input("Enter the meaning: ").lower()
            add_word(unit, word, meaning)
        case "2":
            word = input("Enter the word you want to delete: ").lower()
            delete_word(unit, word)
        case "3":
            old_word = input("Enter the word you want to change as it is written: ").lower()
            new_word = input("Enter the new word: ").lower()
            new_meaning = input("Enter the meaning of the new word: ").lower()
            update_word(unit, old_word, new_word, new_meaning)
        case "4":
            list_words(unit)
        case _:
            exit()
    return None

def create_json_file():
    with open(json_name, 'w') as f:
        json.dump({}, f)

def json_exist():
    return os.path.isfile(json_name)

def word_exist_in_unit(data:json, unit:str, word:str):
    if unit not in data:
        return False
    for entry in data[unit]:
        if entry["word"] == word:
            return True
    return False

def unit_exist_in_data(data:json, unit:str):
    exist = True
    if unit not in data:
        print(f"The unit {unit} does not exist")
        exist = False
    return exist

def add_word(unit:str, word:str, meaning:str):
    with open(json_name, 'r') as f:
        data = json.load(f)
    if unit_exist_in_data(data, unit) == False:
        create_unit_answer = input("Would you like to create it for yes enter 1, if not anything else? ")
        if create_unit_answer != "1":
            print(f"\nThank you very much")
            return None
        data[unit] = []
        
    if word_exist_in_unit(data, unit, word ):
        exist = False
        for entry in data[unit]:
            if entry["word"] == word:
                exist = True
        return exist
    
    new_word = {
    "word" : word,
    "meaning" : meaning
    }
    data[unit].append(new_word)

    with open(json_name, 'w') as f:
        json.dump(data, f, indent=4)
    return None
    

def delete_word(unit:str, word:str):
    with open(json_name, 'r') as f:
        data = json.load(f)

    if unit not in data:
        print(f"There is not a unit with the name {unit}")
    elif word_exist_in_unit(data, unit, word):
        for entry in data[unit]:
            if entry["word"] == word: 
                data[unit].remove(entry)
                break
    
    with open(json_name, 'w') as f:
        json.dump(data, f, indent=4)
    return None

def update_word(unit:str, old_word:str, new_word:str, new_meaning:str):
    with open(json_name, 'r') as f:
        data = json.load(f)

    if unit_exist_in_data(data, unit) and word_exist_in_unit(data, unit, old_word):
        for entry in data[unit]:
            if entry["word"] == old_word:
                entry["word"] = new_word
                entry["meaning"] = new_meaning
                break
        with open(json_name, 'w') as f:
            json.dump(data, f, indent=4) 
    return None

def list_words(unit:str):
    with open(json_name, 'r') as f:
        data = json.load(f)

    if unit_exist_in_data(data, unit):
        for entry in data[unit]:
            print(f"[{entry["word"]}, {entry["meaning"]}]")
    return None