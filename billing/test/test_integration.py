from billing.__main__ import main
import sys


def test_integration(monkeypatch):
    """
    Test that entire solution/process is executed correctly

    Args:
        monkeypatch: Dynamically modify argv to mock expected CLI input
    """

    # Mocking list of CLI arguments to test file data
    monkeypatch.setattr(sys, "argv", ["billing", "example/zone_map.csv", "example/journey_data.csv", "example/output.csv"])

    # Run main() method
    main()

    # Read output csv
    with open(sys.argv[3], "r", encoding="utf-8") as output_file:
        output = output_file.read()

    # Check
    assert output == "user1,3.30\n" "user2,5.00\n" "user3,18.30\n"
