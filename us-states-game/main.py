import turtle
import pandas as pd

FONT = ("Courier", 12, "normal")
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# answer_state = screen.textinput(title = "Guess the State", prompt = "What's another state's name?")

states_data = pd.read_csv("50_states.csv")

t = turtle.Turtle()
t.hideturtle()
t.penup()

guessed_states = []
while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What's another state's name?").title()

    if answer_state == "Exit":
        break

    # print(answer_state)
    match_state = states_data[states_data["state"] == answer_state]
    # print(match_state)
    if not match_state.empty:
        guessed_states.append(answer_state)
        x, y = int(match_state.x.item()), int(match_state.y.item())
        t.goto(x, y)
        t.write(answer_state, False, font = FONT)

# states_to_learn.csv
missed_states = states_data[~states_data["state"].isin(guessed_states)]["state"]
missed_states.to_csv("states_to_learn.csv", index=False)


# if wrong, no counter increment, prompt again

# turtle.mainloop()