from turtle import Turtle, Screen
import pandas

screen = Screen()
screen.title("U.S.States Game")
image = "empty_states_img.gif"
screen.addshape(image)

turtle = Turtle()
turtle.shape(image)

data = pandas.read_csv("D:/Courses_tele/Practical/US_states_game_quiz/50_states.csv")
all_states_to_list = data.state.to_list()
guessed_state = []

while len(guessed_state) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_state)}/50 Correct", prompt="What's the another state name?").title()
    if answer_state == 'Exit':
        #use of list comprehension
        remaining_state = [guess for guess in all_states_to_list if guess not in guessed_state]
        # for guess in all_states_to_list:
        #     if guess not in guessed_state:
        #         remaining_state.append(guess)
        new_data = pandas.DataFrame(remaining_state)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in all_states_to_list:
        guessed_state.append(answer_state)
        t = Turtle()
        t.hideturtle()
        t.penup()
        guess_state = data[data["state"] == answer_state]
        t.goto(int(guess_state.x), int(guess_state.y))
        t.write(answer_state)



