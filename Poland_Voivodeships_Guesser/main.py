import turtle
import pandas

screen = turtle.Screen()
screen.title('Poland Voivodeships Guesser')
screen.setup(height=700, width=700)
screen.bgpic('voivodeships_Poland.gif')

data = pandas.read_csv('16_voivodeship.csv')
all_voivodeships = data.voivodeship.to_list()
guessed_voivodeships = []

while len(guessed_voivodeships) < 16:
    answer_voivodeship = screen.textinput(title=f'{len(guessed_voivodeships)}/16 Voivodeships Correct',
                                          prompt="What's another voivodeship's name?").title()
    if answer_voivodeship == "Exit":
        missing_voivodeships = []
        for voivodeship in all_voivodeships:
            if voivodeship not in guessed_voivodeships:
                missing_voivodeships.append(voivodeship)
        new_data = pandas.DataFrame(missing_voivodeships)
        new_data.to_csv('voivodeships_to_learn.csv')
        break
    if answer_voivodeship in all_voivodeships:
        guessed_voivodeships.append(answer_voivodeship)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        voivodeship_data = data[data.voivodeship == answer_voivodeship]
        t.goto(int(voivodeship_data.x), int(voivodeship_data.y))
        t.write(voivodeship_data.voivodeship.item())
