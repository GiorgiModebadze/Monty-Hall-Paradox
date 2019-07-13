import matplotlib.pyplot as plt
import pandas as pd
from game_definition import game_play

num_tries = int(input('Enter Number of Tries : '))
resutls_list = list()

for i in range(num_tries):
    resutls_list.append(game_play())

change_to_numbers = lambda x: 0 if x == 'Goat' else 1

df = pd.DataFrame(resutls_list).applymap(change_to_numbers)

df['chosen_door_cumulative'] = df['chosen_door'].cumsum()
df['other_door_cumulative'] = df['other_door'].cumsum()

ax = df.chosen_door_cumulative.plot()
ax.set_xlabel("Number of Tries")
ax.set_ylabel("Number of Wins")
ax.set_title("Monty Hall Paradox")

df.other_door_cumulative.plot(ax=ax)
ax.legend(['Win Without Switch', 'Win With Switch'])

last_row = df.tail(1)
wp_without_switch = round(last_row['chosen_door_cumulative'].item() / num_tries * 100, 2)
wp_with_switch = round(last_row['other_door_cumulative'].item() / num_tries * 100, 2)
print(f"Win Probability without switch is {wp_without_switch} % and in case of switch {wp_with_switch} %")

plt.show()
