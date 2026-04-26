import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/results.csv")

# Create result column
def match_result(row):
    if row["home_score"] > row["away_score"]:
        return "Home Win"
    elif row["home_score"] < row["away_score"]:
        return "Away Win"
    else:
        return "Draw"

df["result"] = df.apply(match_result, axis=1)

# 9. Percentage home wins
percentages = df["result"].value_counts(normalize=True) * 100
print("9. Home wins percentage:", percentages["Home Win"])

# 10. Home advantage
print("\n10. Match Outcomes:")
print(percentages)

# 11. Most wins
home_wins = df[df['result'] == 'Home Win']['home_team'].value_counts()
away_wins = df[df['result'] == 'Away Win']['away_team'].value_counts()
total_wins = home_wins.add(away_wins, fill_value=0).sort_values(ascending=False)
print("\n11. Country with most wins:", total_wins.head(1))

# Visualization
plt.figure(figsize=(10,6))
df["total_goals"].hist(bins=15, edgecolor='black')
plt.title("Distribution of Goals Per Match")
plt.xlabel("Total Goals")
plt.ylabel("Number of Matches")
plt.show()