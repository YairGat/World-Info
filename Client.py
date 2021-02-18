# Yair Gat 18.2.2021
# This file represents the client side.
import socket
import PySimpleGUI as sg
import json
from City import City

capitals = City()
capital_arr = capitals.get_cities() # Array of all the cities.
information_type = ['Weather', 'Time', 'Local News']  # All the optional information.
sg.theme('DarkGrey9')
layout = [[sg.Text('Chose city and information type you want to know:')],
          [sg.Listbox(values=capital_arr, size=(30, 6), key='City')],
          [sg.Combo(information_type, key='InfoType')], [sg.Button(button_text='Show Information',
                                                                   enable_events=True)],
          [sg.Button('Exit')]]
window = sg.Window('Information about Cities ', layout)  # Open gui window with title 'information about cities'
HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432  # The port used by the server
while True:  # Event Loop
    event, values = window.read()
    flag = 0  # The flag changes to 1 when the client click on Exit.
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        if event in (sg.WIN_CLOSED, 'Exit'):
            s.send('close'.encode())
            flag = 1
        else:
            data = json.dumps({"City": values['City'][0], "InfoType": values['InfoType']})
            s.send(data.encode())
            data = s.recv(1024).decode('utf-8')
            sg.popup(data)
    if flag == 1:  # True if the client clicked Exit and the program is supposed to end.
        break
window.close()
