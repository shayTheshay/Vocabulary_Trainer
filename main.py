from editing import editing_mode

def main():
    while (True):
        print("-----Vocabulary Trainer-----")
        term = input(f"1 for Editing Mode\n2 for Training Mode\n3 for Testing Mode\nanything else to exit\nEnter: ")
        match term:
            case "1":
                editing_mode()
            case "2":
                print("training_mode()")
            case "3":
                print("testing_mode()")
            case _:
                print("Thank you very much for playin! coms soon.")
                exit()

if __name__ == "__main__":
    main()