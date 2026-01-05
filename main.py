import random

def sping_row():
    symbols = ['🗾', '🍣', '🏯', '🍜','🍙']
    return [random.choice(symbols) for _ in range(3)]

def print_row(list):
    print(" ".join(list))
    bonus_expression(list)
    

def print_result():
    pass

def ten_Times(logo):
    display = logo * 10
    return display


def bonus_expression(list):
    if list[0] == list[1] == list[2]:
        display = ""
        if list[0] == '🗾':
            display =  ten_Times( '🗾')
            print(display)
        if list[0] == '🍣':
            display =  ten_Times( '🍣')
            print(display)
        if list[0] == '🏯':
            display =  ten_Times( '🏯')
            print(display)
        if list[0] == '🍜':
            display =  ten_Times( '🍜')
            print(display)        
        if list[0] == '🍙':
            display =  ten_Times( '🍙')
            print(display)
        else: 
            None

def main():
    print("welcome to the Shoto Slots game!")
    print("Please kill your time when you are waitnng the stable for the room condition")
    print("🗾🍣🏯🍜🍙")

    while True:
        contniue = input("if you want to continue: Press Enter or quit: Enter N:")
        if contniue == "N":
            break
        
        else:
            spin = sping_row()
            print_row(spin)
            continue


if __name__ == "__main__":
    main()