from editing import editing_mode, json_exist
from training import training_mode
from testing import testing_mode

def main():
    while (True):
        print("-----Vocabulary Trainer-----")
        #term = input(f"1 for Editing Mode\n2 for Training Mode\n3 for Testing Mode\nanything else to exit\nEnter: ")
        term = "3"
        match term:
            case "1":
                editing_mode()
            case "2":
                if json_exist():
                    training_mode()
                else:
                    print("Create the words first")
            case "3":
                if json_exist():
                    testing_mode()
                else:
                    print("Create the words first")
            case _:
                print("Thank you very much for playing! come soon.")
                exit()

if __name__ == "__main__":
    main()