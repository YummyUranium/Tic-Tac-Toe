import pandas as pd
import matplotlib.pyplot as plt

file = pd.read_csv("./Artefact/ttt-data.csv")

gamemode_column = file["Gamemode"]
result_column = file["Result"]
winner_column = file["Winner"]
game_length_column = file["Game Length"]
starting_cell_column = file["Starting Cell"]
final_board_state_column = file["Final Board State"]

print("There are", file.shape[0], "games to analyse.")
print("The most common gamemode was", gamemode_column.mode()[0], ".")
print("There was a winner in", result_column.str.split().explode().value_counts()[0], "games.")
print("The most common winner was", winner_column.mode()[0], ", winning a total of", winner_column.str.split().explode().value_counts()[0], "games.")
print("There were", winner_column.str.split().explode().value_counts()[2], "draws.")
print("The average game length was", game_length_column.mean(), "moves")
print("The most common starting cell was cell", starting_cell_column.mode()[0], ", being selected a total of", starting_cell_column.value_counts()[starting_cell_column.mode()[0]], "times.")

fig, axs = plt.subplots(2)
axs[0].title.set_text("Game Results")
axs[0].bar(winner_column.unique(), winner_column.str.split().explode().value_counts())
starting_cell_column.value_counts().plot(title="Starting Cell Distribution", kind="bar")
plt.subplots_adjust(hspace=0.4)
plt.show()