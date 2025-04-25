import csv

# Store temperature records by year
temperature_by_year = {}
# Store combined temperature records by station
temperature_by_station = {}

# Load temperature data from CSV files for each year between 1987 and 2004
for year in range(1987, 2005):
    with open(f"temperatures/stations_group_{year}.csv") as file:
        csv_reader = csv.reader(file)
        next(csv_reader)  # Skip column headers
        # Store each station's monthly temperatures (converted to floats)
        temperature_by_year[year] = {
            row[0]: list(map(float, row[4:])) for row in csv_reader
        }

# Merge temperature data across years by station
for year_data in temperature_by_year.values():
    for station_id, monthly_temps in year_data.items():
        if station_id not in temperature_by_station:
            temperature_by_station[station_id] = []
        # Append current year's monthly temperatures to the station's data
        temperature_by_station[station_id].extend(monthly_temps)

# Compute average temperature for each month across all stations
average_by_month = [0] * 12
for station_temps in temperature_by_station.values():
    for month_index in range(12):
        average_by_month[month_index] += station_temps[month_index]
# Finalize monthly averages
average_by_month = [
    round(total / len(temperature_by_station), 2) for total in average_by_month
]

# Define seasonal groupings by month indices
season_months = {
    "Summer": [11, 0, 1],  # December, January, February
    "Autumn": [2, 3, 4],   # March, April, May
    "Winter": [5, 6, 7],   # June, July, August
    "Spring": [8, 9, 10]   # September, October, November
}
# Calculate seasonal average temperatures
average_by_season = {
    season: round(sum(average_by_month[m] for m in months) / len(months), 2)
    for season, months in season_months.items()
}

# Write seasonal averages to a text file
with open('average_temp.txt', 'a') as file:
    file.write("\n\nSeasonal Average Temperatures:\n")
    for season, avg_temp in average_by_season.items():
        file.write(f"{season}: {avg_temp}\n")

# Identify the station with the widest temperature range
widest_range_station = max(
    temperature_by_station.items(),
    key=lambda x: max(x[1]) - min(x[1])
)
widest_range = round(max(widest_range_station[1]) - min(widest_range_station[1]), 2)

# Save the station with the largest temperature range to a file
with open('largest_temp_range_station.txt', 'w') as file:
    file.write("The Station with Largest Temperature Range is:\n")
    file.write(f"{widest_range_station[0]}: {widest_range}\n")

# Compute average temperature per station
average_by_station = {
    station: sum(temps) / len(temps) for station, temps in temperature_by_station.items()
}
# Identify the warmest and coolest stations
warmest = max(average_by_station.items(), key=lambda x: x[1])
coolest = min(average_by_station.items(), key=lambda x: x[1])

# Write the warmest and coolest stations to a text file
with open('warmest_and_coolest_stations.txt', 'w') as file:
    file.write("Warmest Station:\n")
    file.write(f"{warmest[0]}: {round(warmest[1], 2)}\n\n")
    file.write("Coolest Station:\n")
    file.write(f"{coolest[0]}: {round(coolest[1], 2)}\n")
