import pytest

from billing.process_files import *
from billing.billing_service import BillingService
from billing.test.test_values import test_cases, test_zone_prices


class TestBillingService:
    @pytest.fixture
    def test_billing_service(self):
        """Create a billing service with mock stations and prices for testing.

        Returns:
            A billing service object.
        """
        return BillingService(test_zone_prices)

    def test_process_billing(self, test_billing_service: BillingService):
        """Ensure multiple user journies are processed and returned in correct format

        Keyword args:
            test_billing_service: Test billing service object
        """
        journey_file = "billing/test/test_journey_data.csv"

        assert test_billing_service.process_billing(process_journey_data(journey_file)) == [
            ["5", pytest.approx(2.90)],
            ["adam", pytest.approx(3.30)],
            ["beth", pytest.approx(5.00)],
            ["charlie", pytest.approx(3.60)]
        ]

    @pytest.mark.parametrize("test_input,expected", test_cases)
    def test_calculate_user_billing_amount(self, test_billing_service: BillingService, test_input, expected):
        """Ensure that billing amounts are calculated correctly

        Keyword args:
            test_billing_service -- Test billing service object
            test_input -- List of journies in format ['station_name', 'direction', 'datetime_object']
            expected -- Expected billing amount
        """
        assert test_billing_service.calculate_user_billing_amount(test_input) == expected

    def test_calculate_valid_journey_charge(self, test_billing_service: BillingService):
        """Ensure that calculation for complete journies is correct

        Keyword args:
            test_billing_service -- Test billing service object
        """
        # 2 + 14.9 + 0.8 = 15.9
        assert test_billing_service._calculate_valid_journey_charge('exceed_daily_limit', 'station1') == pytest.approx(17.7)
        # 2 + 0.1 + 0.8 = 2.9
        assert test_billing_service._calculate_valid_journey_charge('station4', 'station1') == pytest.approx(2.9)
