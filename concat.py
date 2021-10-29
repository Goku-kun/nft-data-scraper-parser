import pandas as pd


data_concat = pd.read_csv("set1.csv")


for value in range(2, 16):
    current_data = pd.read_csv(f"set{value}.csv")
    data_concat = pd.concat([data_concat, current_data], ignore_index=True)


data_concat.to_csv("final.csv")
