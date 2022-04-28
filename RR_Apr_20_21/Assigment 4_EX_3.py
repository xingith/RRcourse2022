import us
import os

states = us.states.STATES



def statesUpperLower():
    """all US states in UPPERCASE or lowercase to a file based on needs ."""
    x = input('Please write "u" for uppercase or "l" for lowercase:')
    list = []

    for i in states:
        list.append(i.name)

    dir_path = os.path.join(os.path.dirname(__file__), 'state result')
    os.makedirs(dir_path, exist_ok = True)

    if x == 'u':
        for state in list:
            print(state.upper(), file=open(os.path.join(dir_path, "state_upper.txt"), "a"))
    elif x == 'l':
        for state in list:
            print(state.lower(), file=open(os.path.join(dir_path, "state_lower.txt"), "a"))
    else:
        print('Wrong input! Please write "u" for uppercase or "l" for lowercase:')
        statesUpperLower()

statesUpperLower()