import pandas as pd

# Load data
df = pd.read_csv("data/results.csv")

# 1. Number of matches
print("1. Total matches:", df.shape[0])

# 2. Earliest and Latest year
df['date'] = pd.to_datetime(df['date'])
print("2. Earliest date:", df['date'].min())
print("   Latest date:", df['date'].max())

# 3. Unique countries
total_teams = pd.concat([df['home_team'], df['away_team']]).unique()
print("3. Number of unique countries:", len(total_teams))

# 4. Most frequent home team
most_home = df['home_team'].value_counts().head(1)
print("4. Most frequent home team:", most_home)