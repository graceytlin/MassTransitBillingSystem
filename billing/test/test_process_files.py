from billing import process_files


def test_process_map():
    """
    Test that zone map file is processed correctly
    """
    zone_prices = process_files.process_map('billing/test/test_zone_map.csv')

    # Check
    assert zone_prices["zone1"] == 0.8
    assert zone_prices["zone2"] == 0.5
    assert zone_prices["zone3"] == 0.5
    assert zone_prices["zone4"] == 0.3
    assert zone_prices["zone5"] == 0.3
    assert zone_prices["zone6"] == 0.1
    assert zone_prices["zone7"] == 0.1
    assert zone_prices["zone8"] == 0.1
    assert zone_prices["zone99"] == 0.1


def test_process_journey_data():
    """
    Test that journey data file is read and processed correctly
    """
    user_histories = process_files.process_journey_data('billing/test/test_journey_data.csv')

    # Check that user histories are in alphanumerical order
    assert list(user_histories) == ['5', 'adam', 'beth', 'charlie']

    # Check each user has correct number of journies
    assert len(user_histories["5"]) == 2
    assert len(user_histories["adam"]) == 2
    assert len(user_histories["beth"]) == 1
    assert len(user_histories["charlie"]) == 2

    # Check that datetime has been processed properly - 2022-04-04T9:40:00
    assert user_histories["adam"][0][2].year == 2022
    assert user_histories["adam"][0][2].month == 4
    assert user_histories["adam"][0][2].day == 4

    # Check that station and direction has been processed correctly
    assert user_histories["adam"][0][1] == "IN"
    assert user_histories["adam"][0][0] == "station1"


def test_write_output():
    """
    Test that output is written to file
    """
    test_input = [["test_user", 15.0], ["test_user2", 0.1], ["test_user3", 3.30], ["test_user4", 0]]
    output_file = 'billing/test/test_output.csv'
    process_files.write_output(test_input, output_file)

    # Read output csv
    with open(output_file, "r", encoding="utf-8") as file:
        result = file.read()

    # Check
    assert result == "test_user,15.00\n" "test_user2,0.10\n" "test_user3,3.30\n" "test_user4,0.00\n"
