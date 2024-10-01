import csv
from datetime import datetime

# Map of zones and their prices
zone_price = {
    "1": 0.80,
    "2": 0.50,
    "3": 0.50,
    "4": 0.30,
    "5": 0.30,
    "6": 0.10
}


def process_map(zone_file):
    """Returns a map of station names and the additional associated cost

    Keyword arguments:
        zone_file -- a string containing the file name of a csv file
    """
    print("Processing zone map")
    station_price = {}

    with open(zone_file, 'r', encoding="utf-8") as file:
        reader = csv.reader(file)

        # Skip header row
        next(reader)

        for row in reader:
            station = row[0]
            zone = row[1]

            try:
                station_price[station] = zone_price[zone]  # Set the price of the zone in price map
            except KeyError:
                station_price[station] = zone_price["6"]  # If zone is more than 6, set price to 0.1

    return station_price


def process_journey_data(journey_file):
    """Returns a sorted dictionary of users and their journey data

    Keyword arguments:
        journey_file -- a string containing the file name of a csv file
    """
    print("Processing journey data")
    user_journeys = {}

    with open(journey_file, 'r', encoding="utf-8") as file:
        reader = csv.reader(file)

        # Skip header row
        next(reader)

        for row in reader:
            user_id = row[0]
            station = row[1]
            direction = row[2]
            date = datetime.strptime(row[3], "%Y-%m-%dT%H:%M:%S").date()  # Save date as a datetime object

            if user_id in user_journeys:
                user_journeys[user_id].append([station, direction, date])
            else:
                user_journeys[user_id] = [[station, direction, date]]

    # Sort the dictionary by its keys alphanumerically
    sorted_journeys = dict(sorted(user_journeys.items()))

    return sorted_journeys


def write_output(results, output_file):
    """Writes input to a file

    Keyword arguments:
        output_file -- a string containing the file name of a csv file
    """
    print("Writing output to file")
    with open(output_file, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)

        for user_id, total_charge in results:
            writer.writerow([user_id, format(total_charge, ".2f")])  # Format float to 2 decimal places

    print("Successfully wrote user totals to file: " + output_file)
