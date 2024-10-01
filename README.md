# Programming Project - Mass Transit Billing

## Implementation (High-level overview)

This project consists of one module named ```billing``` which contains a ```BillingService``` class and helper functions

The main function takes two CSV files as input from command-line arguments:

- ```zone_map.csv```: a file of stations and the zones they are in
- ```journey_data.csv```: a file of user transactions in chronological order

The program processes both of these files by first parsing the data, and then sorting the data
from ```journey_data.csv``` by user. A BillingService object is created with the stations and prices provided before
calculating each user's charges for the provided data

The program will then write each user's total charges for the provided data period in an output file with users and
charges in ascending alphanumerical order

## How to run
Extract the folder in its entirety and then run the following to install the required dependencies:

```bash
pip3 install -r requirements.txt
```

From the root of the project:

```bash
python -m billing <path_to_zone_map> <path_to_journey_data> <path_for_output>
```

Example:

```bash
python -m billing example/zone_map.csv example/journey_data.csv example/output.csv
```

## Test implementation

Unit tests are provided for each of the helper functions and ```billing_service.py``` as well as an integration test
which imitates running the program from the command-line

Different scenarios for a user's journey data are provided in ```billing/test/test_values.py``` which emulate what the
program can expect to receive as input and tests that the correct charge is calculated for different journey histories

Test data is also provided for the helper functions to test that files are processed correctly, users are sorted
alphanumerically, and that zone
prices are correctly assigned, for example.

The tests can be ran using ```pytest``` as follows from the root folder:

Example:

```bash
python -m pytest
```

## Assumptions

- The program and tests are ran from the root folder as specified in [How to run](#how-to-run)
- The input files are CSV files encoded in UTF-8 with commas as delimiters
- Inputs are well-formed and valid i.e. no null, missing, or invalid values such as impossible dates
- Input CSV files have headers
- Input journey data is sorted in ascending chronological order so we can ignore the time aspect of the timestamps and
  focus on the order of journeys instead
- Timezone is in UTC (ignoring months when the UK is in BST for example)
- A user entering and exiting at the same station will incur the additional cost of that station twice
- Users must exit before re-entering for journeys to be valid
- Journey data can span years/months and is not limited to any period of time
- A station zone will be a non-negative integer
- A station can only be in one zone

## Functional Requirements

- The program will output total charges for each customer for the provided period of journey data
- The program takes command line arguments as described above
- The program will calculate the charges based on the following rules:
    - A complete journey is when a user has a corresponding ```OUT``` journey for an ```IN``` journey
    - Each complete journey has a £2 base fee, and additional costs based on the entry and exit zones.
    - Erroneous journeys where an In or OUT is missing will be charged at £5 as the total journey price
    - All complete journeys should be completed before midnight (i.e. all valid journeys will have an IN and an OUT on
      the same day)
    - There is a daily cap of £15 and a monthly cap of £100
    - Once the cap is reached, the customer will not incur extra charges for the given day or month

| Zone | In / Out additional Cost |
|------|--------------------------|
| 1    | £0.80                    |
| 2-3  | £0.50                    |
| 4-5  | £0.30                    |
| 6+   | £0.10                    |

## Non-Functional Requirements

- The program is written in Python
- The program only uses the Python standard library
- The program provides tests and comments for clarity and best practice
