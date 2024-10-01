from billing.constants import *


class BillingService:
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self, zone_prices):
        self.zone_prices = zone_prices

    def __repr__(self) -> str:
        return f"{type(self).__name__}(zone_prices={self.zone_prices})"

    def process_billing(self, user_history):
        """Returns a list of users and their total billing amounts

        Keyword arguments:
            user_history -- an ordered dictionary with user_id as key and list of journey data as the values
        """
        print("Calculating user balances")
        billing_amounts = []
        for user in user_history:
            total_amount = self.calculate_user_billing_amount(user_history[user])
            billing_amounts.append([user, total_amount])
        return billing_amounts

    def calculate_user_billing_amount(self, journey_history) -> float:
        """Returns the total charge amount for a given list of entry/exit data

        Keyword arguments:
            journey_history -- a list of journies in the format ['station_name','direction',datetime_object]
        """
        total_amount = 0.00
        daily_total = 0.00
        monthly_total = 0.00

        # Marker to track the current datetime
        current_date = journey_history[0][2]

        # Entry station tracker
        entry_station = []

        for station, direction, timestamp in journey_history:
            # Check if the month, or year, has changed, then check if the day has changed
            if timestamp.month != current_date.month or timestamp.year > current_date.year:
                # Check for open-ended journey, add error fee, and reset markers
                if entry_station:
                    daily_total += ERROR_FEE
                    entry_station = []
                current_date = timestamp

                # Add monthly total amount or monthly cap if exceeded to total amount
                total_amount += min(MONTHLY_CAP, monthly_total)
                # Reset monthly total tracker
                monthly_total = 0.00
            elif timestamp > current_date:
                # Check for open-ended journey, add error fee, and reset markers
                if entry_station:
                    daily_total += ERROR_FEE
                    entry_station = []
                current_date = timestamp

                # Add daily total amount or daily cap if exceeded to monthly total
                monthly_total += min(DAILY_CAP, daily_total)
                # Reset daily total tracker
                daily_total = 0.00

            # Logic to process valid and invalid journies
            if not entry_station and direction == "IN":
                # Valid entry - save entry leg
                entry_station.append(station)
            elif not entry_station and direction == "OUT":
                # Invalid journey - apply invalid journey fee
                daily_total += ERROR_FEE
            elif entry_station and direction == "IN":
                # Invalid entry - apply invalid journey fee and reset entry marker
                daily_total += ERROR_FEE
                entry_station.pop()
                entry_station.append(station)
            elif entry_station and direction == "OUT":
                # Valid journey path - Add base fee and station fee - reset entry marker
                daily_total += self._calculate_valid_journey_charge(entry_station.pop(), station)
                entry_station = []

        # Check if last journey was open-ended and add error fee
        if entry_station:
            daily_total += ERROR_FEE

        # Add the totals or cap if cap exceeded
        monthly_total += min(DAILY_CAP, daily_total)
        total_amount += min(MONTHLY_CAP, monthly_total)

        return total_amount

    def _calculate_valid_journey_charge(self, entry_station, exit_station):
        """Helper function to calculate the total fee of a valid journey

        Keyword arguments:
            entry_station -- The station from which the user entered in from
            exit_station -- The station from which the user exited from
        """
        total_fee = BASE_FEE + self.zone_prices[entry_station] + self.zone_prices[exit_station]
        return total_fee
