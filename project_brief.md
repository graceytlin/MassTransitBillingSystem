# Project brief

## Technical requirements
- Python standard library only
- No third-party libraries beside common test packages (e.g. pytest or testify)
- Production-quality code - tests and comments where necessary.
- Program should be able to be ran using the command line arguments described below.

## Business requirements
The transit system has a network of train stations, each belonging to a pricing zone.
Each time a user enters (IN) or exits (OUT) a station it is recorded.

The data is recorded at each station with a user_id, direction (either IN or OUT
of the station), the station and the time of the entry/exit (in UTC) for all the journeys in a given
time period.

The data is sorted by timestamp, but not necessarily by users. The MassTransitBillingSystemApp calculates the total charge for each customer at the end of the period.

Each journey has a £2 base fee, and additional costs based on the entry and exit zones.

| Zone | In / Out additional Cost |
| ---- | ------------------------ |
| 1    | £0.80                    |
| 2-3  | £0.50                    |
| 4-5  | £0.30                    |
| 6+   | £0.10                    |

Examples: The price of a journey from zone 1 to zone 1 is 2.00 + 0.80 + 0.80 = £3.60. The price of a
journey from zone 6 to zone 4 is 2.00 + 0.10 + 0.30 = £2.40.

For any erroneous journeys where an IN or OUT is missing, a £5 fee is used as the total journey
price. All valid journeys are completed before midnight (i.e. all valid
journeys will have an IN and an OUT on the same day).

There is also a daily cap of £15, and a monthly cap of £100. Caps include all journey costs and
fees, and once a given cap is reached the customer pays no extra for the given day or month.

Expected cmd to run the application:
```bash
<your_program> <zones_file_path> <journey_data_path> <output_file_path>
```

Expected Output: each user_id and their billing_amount (to 2 decimal places) written to
<output_file_path> in user_id alphanumeric increasing order(e.g. ['23Charlie', 'alpha', 'bravo']) as
shown in the example output file.

To run this Python application:
```bash
python my_solution.py zone_map.csv journey_data.csv output.csv
```