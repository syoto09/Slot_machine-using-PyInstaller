import random

def sping_row():
    symbols = ['🗾', '🍣', '🏯', '🍜','🍙']
    return [random.choice(symbols) for _ in range(3)]

def print_row(list):
    print(" ".join(list))
    

def print_result():
    pass


def bonus_expression(list):
    if list[0] == list[1] == list[2]:
        if list[0] == '🗾':
            print("🗾🗾🗾🗾🗾🗾🗾🗾🗾🗾🗾🗾🗾🗾🗾🗾🗾🗾🗾🗾🗾")


def main():
    print("welcome to the Shoto Slots game!")
    print("Please kill your time when you are waitnng the stable for the room condition")
    print("🗾🍣🏯🍜🍙")

    while True:
        contniue = input("if you want to continue: Enter Y & quit: Enter: N:")
        if contniue == "N":
            break
        
        else:
            spin = sping_row()
            print_row(spin)
            continue


if __name__ == "__main__":
    main()