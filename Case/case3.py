import requests
import json
import os

url = 'https://5hyqtreww2.execute-api.eu-north-1.amazonaws.com/artists/'

r = requests.get(url)
list_artist = json.loads(r.text)

x = list_artist['artists'][1]['id']
url2 = url + x

f = requests.get(url2)
artist_info = json.loads(f.text)

ui_width = 36
dotted_line = '*' * ui_width
dashed_line = '-' * ui_width

while True:
    print(f'''
{dashed_line}
        Artist Database
{dashed_line}

|L| List Artists
|V| View Artist Profile
|E| Exit application
{dashed_line}
    ''')

    choice = input('Selection > ').lower()

    if choice == 'l':
        os.system('cls')
        for artist in list_artist['artists']:
            print('| ', artist['name'])
        print(f'{dashed_line}')
        input('Press enter to continue')
    elif choice == 'e':
        break
    elif choice == 'v':
        print(f'''
{dotted_line}
            {str(artist_info['artist']['name'])}
{dotted_line}
| Members:      {''.join(artist_info['artist']['members'])}
| Genres:       {''.join(artist_info['artist']['genres'])}
| Years Active: {''.join(artist_info['artist']['years_active'])}
{dashed_line}
''')
        input('Press enter to continue')