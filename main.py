

def main():
    while (True):
        term = input(f"1 for Editing Mode\n2 for Training Mode\n3 for Testing Mode\nanything else to exit\nEnter: ")
        match term:
            case "1":
                print("editing_mode()")
            case "2":
                print("training_mode()")
            case "3":
                print("testing_mode()")
            case _:
                exit()

if __name__ == "__main__":
    main()