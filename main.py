# Will Snyder
# 1/16/21

import random

import PySimpleGUI as sg

layout = [[sg.Text("Guess a number between 0 and 100.")],
          [sg.Input()],
          [sg.Button('Ok')]]

window = sg.Window('Number Guesser', layout)

target = random.randint(0, 100)
count = 1

running = True

while running:
    event, values = window.read()

    valueConvert = str(values)
    split = valueConvert.split("'")
    splitGet = split[1]

    cur = int(splitGet, 10)

    if cur == target:
        window.close()

        final = str(count)
        doneLayout = [[sg.Text("Correct! It took you " + final + " tries to guess the correct number")],
                      [sg.Button('Ok')]]

        window = sg.Window('Number Guesser', doneLayout)

        if event in [sg.Button('Ok')]:
            window.close

    elif cur != target:
        if cur > target:
            window.close()

            greaterLayout = [[sg.Text("Try again. The target is less than your number.")],
                             [sg.InputText()],
                             [sg.Button('Ok')]]

            window = sg.Window('Number Guesser', greaterLayout)

        elif cur < target:
            window.close()
            lessLayout = [[sg.Text('Try again. The target is greater than your number.')],
                          [sg.InputText()],
                          [sg.Button('Ok')]]

            window = sg.Window('Number Guesser', lessLayout)

        count = count + 1

window.close()
