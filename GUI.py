import PySimpleGUI as sg

from City import City, Madrid, Jerusalem

sg.theme('DarkGrey9')
# layout = [[sg.Text('Theme Browser')],
#           [sg.Text('Click a Theme color to see demo window')],
#           [sg.Listbox(values=sg.theme_list(), size=(20, 12), key='-LIST-', enable_events=True)],
#           [sg.Button('Exit')]]
layout = [[sg.Text('Information about capitals')],
          [sg.Listbox(values=['Jerusalem', 'Madrid'], size=(30, 6), key='Capital')],
          [sg.Combo(['Weather', 'Time', 'Local News'], key='InfoType')], [sg.Button(button_text='Show Information',
                                                                                    enable_events=True)],
          [sg.Button('Exit')]]
window = sg.Window('Capital ', layout)

while True:  # Event Loop
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Exit'):
        break
    if (values['Capital'][0] is not None) and (values['InfoType'][0] is not None):
        sg.popup(str(values['Capital']) + " " + str(values['InfoType']))
    else:
        sg.popup("Please chose capital and information you want to see")

window.close()


class GUI:
    def __init__(self):
        self.capitals = ['Jerusalem', 'Madrid']
        self.information_type = ['Weather', 'Time', 'Local News']

    def get_capitals(self):
        return self.capitals

    def get_information_type(self):
        return self.information_type

    def play(self):
        sg.theme('DarkGrey9')
        layout = [[sg.Text('Information about capitals')],
                  [sg.Listbox(values=self.get_capitals(), size=(30, 6), key='Capital')],
                  [sg.Combo(self.get_information_type(), key='InfoType')],
                  [sg.Button(button_text='Show Information',
                             enable_events=True)],
                  [sg.Button('Exit')]]
        window = sg.Window('Information about capitals ', layout)

        while True:  # Event Loop
            event, values = window.read()
            if event in (sg.WIN_CLOSED, 'Exit'):
                break
            if (values['Capital'][0] is not None) and (values['InfoType'][0] is not None):
                sg.popup(str(values['Capital']) + " " + str(values['InfoType']))
            else:
                sg.popup("Please chose capital and information you want to see")
