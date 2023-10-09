width = 40

def lines(dash=True):
    if dash == False:
        print('*'*width)
    else:
        print('-'*width)

def main():
    lines()
    print('Artist Database'.center(width))
    lines()

def error(sel,name=False):
    lines()
    print(f'''|
| ERROR: Unknown command '{sel}'
|''')
    lines()
    if name == False:
        input('Press enter to continue...')

def view(name):
    lines(False)
    print(f'{name["artist"]["name"]}'.center(width))
    lines(False)
    print(f'''| Members:      {', '.join(name["artist"]["members"])}
| Genres:       {', '.join(name["artist"]["genres"])}
| Years active: {', '.join(name["artist"]["years_active"])}''')
    lines()

def select():
    print('''| L | List artists
| V | View artist profile
| E | Exit application''')
    lines()