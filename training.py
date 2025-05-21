from editing import unit_exist_in_data, word_exist_in_unit
from constants import load_vocab


def training_mode():
    print(f"\nTraining Mode")
    term = input(f"1 for training by unit\n2 for training by range of words in unit\nanything else to go back\nEnter: ")
    if term in ("1" , "2"):
        list_units_words()
        data = load_vocab()
        unit:str = input("Enter the unit for the training: ").lower()
        if not unit_exist_in_data(data, unit):
            print(f"The unit {unit} does not exist in data.")

        else:
            match term:
                case "1":
                    print_words_in_unit(unit)
                case "2":
                    start_word = input("From which word would you like to start? ").lower()
                    end_word = input("On which word would you like to end? ").lower()
                    print_range_words_in_unit(unit, start_word, end_word)
    else:
        print("Exit training mode")
    return None

def print_words_in_unit(unit:str): 
    data = load_vocab()
    for unit_name, words_in_unit in data.items():
        if unit_name == unit:
            print("The training begins!:")
            for word in words_in_unit:
                print(f"{word['word']}")
                input("Press enter to see meaning")
                print(f"{word['meaning']}")
    return None
                
def print_range_words_in_unit(unit:str, start_word:str, end_word:str):
    data = load_vocab()
    conditions_met = check_word_range_conditions_met(data, unit, start_word, end_word)
    
    if conditions_met == True:
        start_flag = False
        end_flag = False
        for word in data[unit]:
            if word['word'] == start_word:
                start_flag = True
            if start_flag == True and end_flag == False:
                print(f"{word['word']} - ")
                input("Press enter to see meaning")
                print(f"{word['meaning']}")
                if word['word'] == end_word:
                    end_flag = True

        print(f"You finished training for unit:{unit}")
    else:
        print("Notice the error you recieved, it will explain why the program has continued")

    return None

def list_units_words():
    data = load_vocab()
    for unit_name, words_list in data.items():
        print(f"Unit_name = {unit_name}")
        for word in words_list:
            print(f"- {word['word']}")
    return None

def check_word_range_conditions_met(data:str, unit:str, start_word:str, end_word:str):
    data = load_vocab()
    if word_exist_in_unit(data, unit, start_word) and word_exist_in_unit(data, unit, end_word):
        if check_start_end_words_in_order(data, unit, start_word, end_word):
            return True
        else:
            print("Please make sure the words are in the correct order")
    else:
        print("Please make sure the words exist")
    return False

def check_start_end_words_in_order(data:str, unit:str, start_word:str, end_word:str):
    flag=False
    for unit_name, words_in_unit in data.items():
        if unit_name == unit:
            for word in words_in_unit:
                if word['word'] == start_word:
                    flag = True
                elif flag == True and word['word'] == end_word:
                    return True
    print("The order of the words is not correct, pleae make sure start is before end words")
    return False



    
