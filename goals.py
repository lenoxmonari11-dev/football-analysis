import pandas as pd
import numpy as np

df = pd.read_csv("data/results.csv")
df["total_goals"] = df["home_score"] + df["away_score"]

# 5. Average goals
print("5. Average goals per match:", df["total_goals"].mean())

# 6. Highest scoring match
max_index = df["total_goals"].idxmax()
print("6. Highest scoring match:")
print(df.loc[max_index][['home_team', 'away_team', 'home_score', 'away_score']])

# 7. Home vs Away goals
print("7. Total home goals:", df["home_score"].sum())
print("   Total away goals:", df["away_score"].sum())

# 8. Most common total goals
print("8. Most common total goals:", df["total_goals"].mode()[0])