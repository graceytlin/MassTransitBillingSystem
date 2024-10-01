from datetime import datetime

test_zone_prices = {
    'station1': 0.80,
    'station2': 0.50,
    'station3': 0.30,
    'station4': 0.10,
    'exceed_daily_limit': 14.90
}

# Test case for a complete journey - 2 + 0.8 + 0.5
complete_journey = [
    ['station1', 'IN', datetime(2022, 4, 4)],
    ['station2', 'OUT', datetime(2022, 4, 4)]
]

# Test cases for incomplete journies - 5.0
incomplete_journey_in = [['station1', 'IN', datetime(2022, 4, 4)]]
incomplete_journey_out = [['station2', 'OUT', datetime(2022, 4, 4)]]
incomplete_different_day = [
    ['station3', 'IN', datetime(2022, 4, 3)],  # Incomplete - 5.0
    ['station2', 'OUT', datetime(2022, 4, 4)]  # Incomplete - 5.0
]

# Test case for reaching daily cap - (2 + 14.9 + 0.8) = 15.0
daily_cap = [
    ['exceed_daily_limit', 'IN', datetime(2022, 4, 5)],
    ['station1', 'OUT', datetime(2022, 4, 5)]
]

# Complex test cases for reaching daily cap
daily_cap_incomplete = [
    ['station2', 'IN', datetime(2022, 4, 5)],
    ['station1', 'OUT', datetime(2022, 4, 5)],  # Complete journey - 3.3
    ['station3', 'OUT', datetime(2022, 4, 5)],  # Incomplete journey - 5.0
    ['station1', 'IN', datetime(2022, 4, 5)],  # Incomplete journey - 5.0
    ['exceed_daily_limit', 'IN', datetime(2022, 4, 5)],
    ['station2', 'OUT', datetime(2022, 4, 5)]  # Complete journey - > 15.0
]

# Test cases for multiple days
multiple_days = [
    ['station1', 'IN', datetime(2022, 4, 3)],
    ['station3', 'OUT', datetime(2022, 4, 3)],  # Complete journey - 3.1
    ['station4', 'IN', datetime(2022, 4, 4)],
    ['station3', 'OUT', datetime(2022, 4, 4)]  # Complete journey - 2.4
]

complex_multiple_days = [
    ['exceed_daily_limit', 'IN', datetime(2022, 4, 3)],
    ['station1', 'OUT', datetime(2022, 4, 3)],  # Daily limit - 15.0
    ['station1', 'IN', datetime(2022, 4, 4)],  # Incomplete - 5.0
    ['station2', 'OUT', datetime(2022, 4, 5)],  # Incomplete - 5.0
    ['station4', 'IN', datetime(2022, 4, 5)],  # Incomplete - 5.0
    ['station4', 'IN', datetime(2022, 4, 5)],
    ['station2', 'OUT', datetime(2022, 4, 5)],  # Complete - 2.6
    ['station4', 'IN', datetime(2022, 4, 6)],
    ['exceed_daily_limit', 'OUT', datetime(2022, 4, 6)]  # Daily limit - 15.0
]

# Test cases for multiple months
multiple_months = [
    ['station1', 'IN', datetime(2022, 4, 3)],
    ['station3', 'OUT', datetime(2022, 4, 3)],  # Complete journey - 3.1
    ['station4', 'IN', datetime(2022, 5, 3)],
    ['station3', 'OUT', datetime(2022, 5, 3)]  # Complete journey - 2.4
]

# Test case for exceeding monthly cap (15*7)
monthly_cap = [
    ['exceed_daily_limit', 'IN', datetime(2022, 4, 3)],
    ['exceed_daily_limit', 'OUT', datetime(2022, 4, 3)],  # Day 1
    ['exceed_daily_limit', 'IN', datetime(2022, 4, 4)],
    ['exceed_daily_limit', 'OUT', datetime(2022, 4, 4)],  # Day 2
    ['exceed_daily_limit', 'IN', datetime(2022, 4, 5)],
    ['exceed_daily_limit', 'OUT', datetime(2022, 4, 5)],  # Day 3
    ['exceed_daily_limit', 'IN', datetime(2022, 4, 6)],
    ['exceed_daily_limit', 'OUT', datetime(2022, 4, 6)],  # Day 4
    ['exceed_daily_limit', 'IN', datetime(2022, 4, 7)],
    ['exceed_daily_limit', 'OUT', datetime(2022, 4, 7)],  # Day 5
    ['exceed_daily_limit', 'IN', datetime(2022, 4, 8)],
    ['exceed_daily_limit', 'OUT', datetime(2022, 4, 8)],  # Day 6
    ['exceed_daily_limit', 'IN', datetime(2022, 4, 9)],
    ['exceed_daily_limit', 'OUT', datetime(2022, 4, 9)]  # Day 7
]

# Test case for journies a year apart
multiple_years = [
    ['station1', 'IN', datetime(2022, 4, 3)],
    ['station3', 'OUT', datetime(2022, 4, 3)],  # Complete journey - 3.1
    ['station4', 'IN', datetime(2023, 4, 3)],
    ['station3', 'OUT', datetime(2023, 4, 3)]  # Complete journey - 2.4
]

test_cases = [
    (complete_journey, 3.3),
    (incomplete_journey_in, 5.0),
    (incomplete_journey_out, 5.0),
    (incomplete_different_day, 10.0),
    (daily_cap, 15.0),
    (daily_cap_incomplete, 15.0),
    (multiple_days, 5.5),
    (complex_multiple_days, 47.6),
    (multiple_months, 5.5),
    (monthly_cap, 100.0),
    (multiple_years, 5.5)
]
