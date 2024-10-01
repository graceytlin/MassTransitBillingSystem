import sys
from billing.process_files import *
from billing.billing_service import BillingService


def main():
    """Main function to process CLI arguments and write to file
    """
    zone_file, journey_file, output_file = sys.argv[1:]

    # Parse zone map and journey data
    stations = process_map(zone_file)
    user_journeys = process_journey_data(journey_file)

    billing_service = BillingService(stations)

    # Process the journey data and calculate user totals
    user_charges = billing_service.process_billing(user_journeys)

    # Write total charges per user to output file
    write_output(user_charges, output_file)


if __name__ == "__main__":
    main()
