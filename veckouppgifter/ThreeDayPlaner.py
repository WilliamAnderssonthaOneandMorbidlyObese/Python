# import libraries
import os

# varibles
today = "Run 5 km"
tomorrow = "Lift 10 kg"
later = "Cycle 30 km"

# while containing everything
while True:
    # emtiying the concole
    os.system("cls")

# print ui
    print(f'''.: THREE DAY PLANNER :.
-----------------------
TODAY:    {today}
TOMORROW: {tomorrow}
LATER:    {later}
-----------------------
n | Next day
c | Change goal
e | Exit program
----------------------- ''')
    # take input
    command = input("command > ")

    # if for command and elif'
    if command == 'c':
        os.system("cls")
        # choose a day ui
        print(f'''.: THREE DAY PLANNER :.
-----------------------
You chose change goal.
-----------------------
Pick goal to change
0 | Today
1 | Tomorrow
2 | Later
-----------------------''')
        # if for day choise
        change = input('Change goal >')
        if change == '0':
            today = input('To what >')
        elif change == '1':
            tomorrow = input('To what >')
        elif change == '2':
            later = input('To what >')
            # elif command
        else:
            print('''-----------------------
ERROR: Bad day
INFO:  Expected integer (0-2)
-----------------------''')
            input('Press enter to continue...')
    elif command == 'n':
        today = tomorrow
        tomorrow = later
        later = ''
    elif command == 'e':
        break
    else:
        print(f'''-----------------------
ERROR: Invalid input ({command})
-----------------------''')
        input('Press enter to continue...')
