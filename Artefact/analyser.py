import pandas as pd
import matplotlib.pyplot as plt

# Declares file and stores columns as variables
file = pd.read_csv("./Artefact/ttt-data.csv")

gamemode_column = file["Gamemode"]
result_column = file["Result"]
winner_column = file["Winner"]
game_length_column = file["Game Length"]
starting_cell_column = file["Starting Cell"]
final_board_state_column = file["Final Board State"]

# Displays stats about data set
print("There are", file.shape[0], "games to analyse.")
print("The most common gamemode was", gamemode_column.mode()[0], ".")
print("There was a winner in", result_column.str.split().explode().value_counts()[0], "games.")
print("The most common winner was", winner_column.mode()[0], ", winning a total of", winner_column.str.split().explode().value_counts()[0], "games.")
print("There were", winner_column.str.contains('None').sum(), "draws.")
print("The average game length was", game_length_column.mean(), "moves")
print("The most common starting cell was cell", starting_cell_column.mode()[0], ", being selected a total of", starting_cell_column.value_counts()[starting_cell_column.mode()[0]], "times.")

# Makes the x axis for winner graph
winner_axis = file.groupby("Winner")["Winner"].count().reset_index(
  name='Count').sort_values(['Count'], ascending=False)

winner_axis = pd.Series(winner_axis.iloc[:, 0])

# Creates two subplots and displays them
fig, axs = plt.subplots(2)
axs[0].title.set_text("Game Results")
axs[0].bar(winner_axis, winner_column.str.split().explode().value_counts())
starting_cell_column.value_counts().plot(title="Starting Cell Distribution", kind="bar")
plt.subplots_adjust(hspace=0.4)
plt.show()