import PySimpleGUI as sg

questions = [
    "Where did this 1 in front of phone numbers come from? Explain like I'm five.",
    "Who painted the Mona Lisa?",
    "What is the largest planet in our solar system?"
]

answers = [
    ["The 1 in front of phone numbers is called a country code, and it is used to identify which country a phone "
     "number belongs to. This is especially important when making international phone calls, because it helps the "
     "phone system route the call to the correct country. The use of country codes for phone numbers started when "
     "telephone systems were first developed in the late 1800s and early 1900s. At that time, each country had its "
     "own telephone system, and it was important to be able to distinguish between different countries when making "
     "phone calls. The 1 in front of phone numbers in the United States is the country code for the United States.", "London"],
    ["Leonardo da Vinci", "Pablo Picasso"],
    ["Jupiter", "Saturn"]
]

question_index = 0

layout = [
    [sg.Text(questions[question_index], key='question')],
    [sg.Radio(answers[question_index][0], 'Q', key='option1')],
    [sg.Radio(answers[question_index][1], 'Q', key='option2')],
    [sg.Button('Submit')]
]

window = sg.Window('Quiz', layout, margins=(150, 150))
question_index += 1

while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED:
        break
    elif event == 'Submit':
        selected_answer = values['option1'] if values['option1'] else values['option2']

        question_index += 1
        if question_index < len(questions):
            window['question'].update(questions[question_index])
            window['option1'].update(text=answers[question_index][0])
            window['option2'].update(text=answers[question_index][1])
        else:
            break

window.close()

