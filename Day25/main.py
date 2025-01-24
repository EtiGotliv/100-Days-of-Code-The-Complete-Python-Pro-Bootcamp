import turtle

import pandas as pd

BG_IMAGE = "blank_states_img.gif"
INPUT_CSV_FILE = "50_states.csv"
OUTPUT_CSV_FILE = "states_to_learn.csv"
FONT = ("Arial", 10, "normal")


def add_label(entry):
    new_turtle = turtle.Turtle()
    new_turtle.hideturtle()
    new_turtle.penup()
    new_turtle.speed(0)
    new_turtle.setx(entry.x.item())
    new_turtle.sety(entry.y.item())
    new_turtle.write(entry.state.item(), align="left", font=FONT)



screen = turtle.Screen()
screen.setup(width=725, height=491)
screen.title("U.S. States Game")
screen.bgpic(BG_IMAGE)

df = pd.read_csv(INPUT_CSV_FILE)
all_states = df.state.tolist()
states_count = len(all_states)
revealed_states = []

title_text = "Guess the state"
prompt_text = "Enter a state name"

game_is_over = False
while not game_is_over:
    answer = screen.textinput(title=title_text, prompt=prompt_text).title()
    if answer == "Exit":
        game_is_over = True
    elif answer in all_states and answer not in revealed_states:
        add_label(df[df.state == answer])
        revealed_states.append(answer)

    revealed_count = len(revealed_states)
    if revealed_count > 0:
        title_text = f"{revealed_count}/{states_count} states correct"
        prompt_text = "Enter another state name"

    if revealed_count == states_count:
        game_is_over = True

if len(revealed_states) == 0:
    print("You didn't guess a single state.")
elif len(revealed_states) == states_count:
    print("Well done, you've entered all states.")
else:
    missed_states = []
    for state in all_states:
        if state not in revealed_states:
            missed_states.append(state)
    pd.DataFrame(missed_states).to_csv(OUTPUT_CSV_FILE)
    print(f"The {len(missed_states)} missing states have been saved to {OUTPUT_CSV_FILE}.")