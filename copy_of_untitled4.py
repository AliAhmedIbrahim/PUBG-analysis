# -*- coding: utf-8 -*-
"""Copy of Untitled4.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1HGXxuIpxybHzP6IWS33qYV1rKHoBZQwo
"""

import pandas as pd

file_path = 'Pubg_Stats.csv'
pubg_data = pd.read_csv(file_path)

pubg_data.head()

import pandas as pd
import matplotlib.pyplot as plt

file_path = 'Pubg_Stats.csv'
pubg_data = pd.read_csv(file_path)

if 'Weapon Type' in pubg_data.columns:
    weapon_type_counts = pubg_data['Weapon Type'].value_counts()
    plt.figure(figsize=(12, 6))
    weapon_type_counts.plot(kind='bar', color='skyblue')
    plt.title('Distribution of Weapon Types')
    plt.xlabel('Weapon Type')
    plt.ylabel('Count')
    plt.xticks(rotation=45)
    plt.show()
else:
    print("The column 'Weapon Type' does not exist in the dataset.")

plt.figure(figsize=(12, 6))
plt.hist(pubg_data['Matches_Played'], bins=30, color='skyblue', edgecolor='black')
plt.title('Distribution of Matches Played')
plt.xlabel('Matches Played')
plt.ylabel('Count')
plt.show()

top_players_kills = pubg_data.nlargest(10, 'Kills')

plt.figure(figsize=(12, 6))
plt.bar(top_players_kills['Player_Name'], top_players_kills['Kills'], color='salmon')
plt.title('Top 10 Players by Kills')
plt.xlabel('Player Name')
plt.ylabel('Kills')
plt.xticks(rotation=45)
plt.show()