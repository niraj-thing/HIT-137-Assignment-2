import os
import pandas as pd
from collections import defaultdict

# Directory where the CSV files are stored
DATA_DIR = "temperatures"

# Function to determine season based on month (Australia-specific)
def get_season(month):
    if month in [12, 1, 2]:
        return 'Summer'
    elif month in [3, 4, 5]:
        return 'Autumn'
    elif month in [6, 7, 8]:
        return 'Winter'
    else:
        return 'Spring'

# Load all CSV files into one DataFrame
def load_data():
    all_data = []
    for file in os.listdir(DATA_DIR):
        if file.endswith(".csv"):
            df = pd.read_csv(os.path.join(DATA_DIR, file))
            all_data.append(df)
    return pd.concat(all_data, ignore_index=True)

def process_data(df):
    df['date'] = pd.to_datetime(df['date'])
    df['month'] = df['date'].dt.month
    df['season'] = df['month'].apply(get_season)

    # 1. Average temperature by season
    season_avg = df.groupby('season')['temperature'].mean().round(2)
    with open("average_temp.txt", "w") as f:
        for season in ['Summer', 'Autumn', 'Winter', 'Spring']:
            temp = season_avg.get(season, "N/A")
            f.write(f"{season}: {temp}°C\n")

    # 2. Station(s) with largest temperature range
    station_stats = df.groupby('station_id')['temperature'].agg(['min', 'max'])
    station_stats['range'] = station_stats['max'] - station_stats['min']
    max_range = station_stats['range'].max()
    stations_with_max_range = station_stats[station_stats['range'] == max_range].index.tolist()
    with open("largest_temp_range_station.txt", "w") as f:
        f.write(f"Largest temperature range: {max_range:.2f}°C\n")
        f.write("Station(s):\n")
        for station in stations_with_max_range:
            f.write(f"- {station}\n")

    # 3. Warmest and coolest stations (based on average)
    avg_temps = df.groupby('station_id')['temperature'].mean()
    max_avg = avg_temps.max()
    min_avg = avg_temps.min()
    warmest = avg_temps[avg_temps == max_avg].index.tolist()
    coolest = avg_temps[avg_temps == min_avg].index.tolist()
    with open("warmest_and_coolest_station.txt", "w") as f:
        f.write(f"Warmest average temperature: {max_avg:.2f}°C\n")
        f.write("Warmest station(s):\n")
        for station in warmest:
            f.write(f"- {station}\n")
        f.write(f"\nCoolest average temperature: {min_avg:.2f}°C\n")
        f.write("Coolest station(s):\n")
        for station in coolest:
            f.write(f"- {station}\n")

if __name__ == "__main__":
    df = load_data()
    process_data(df)
