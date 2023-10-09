import json
import requests
import ui
import os

apiurl = 'https://5hyqtreww2.execute-api.eu-north-1.amazonaws.com/artists/'

def clear():
    os.system('cls' if os.name == 'nt' else 'clear' )

def request():
    global respons
    request = requests.get(apiurl)
    respons = json.loads(request.text)
    
def requestinfo(id):
    global responsinfo
    requestinfo = requests.get(apiurl + id)
    responsinfo = json.loads(requestinfo.text)

def list():
    request()
    for a in respons['artists']:
        print('| ', a['name'])
    ui.lines(False)

def view():
    nameinput = input('| Artist name > ').title()
    request()
    if any(a['name'] == nameinput for a in respons['artists']):
        for a in respons['artists']:
            if a['name'] == nameinput:
                requestinfo(a['id'])
                ui.view(responsinfo)
    else:
        ui.error(nameinput,True)

def clearnprint():
    clear()
    ui.main()
    ui.select()

select = {'v':view,'l':list }

clearnprint()
while True:
    selection = input('| Selection > ').lower()
    if selection in select:
        clear()
        ui.main()
        select[selection]()
        ui.select()
    elif selection == 'e':
        clear()
        print('\nSUCCESS: Script exited successfully!')
        break
    else:
        ui.error(selection)
        clearnprint()