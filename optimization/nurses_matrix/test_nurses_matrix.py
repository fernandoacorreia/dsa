from nurses_matrix import Nurse, Scheduler
import pytest

@pytest.mark.parametrize("params", [
    (
        {
            'nurses': [
                Nurse("Alice", 4),
                Nurse("Bob", 3),
                Nurse("Charlie", 2),
                Nurse("Diana", 1),
                Nurse("Eve", 3),
                Nurse("Felix", 4),
                Nurse("George", 2),
                Nurse("Hector", 3)
            ],
            'days': 7,
            'shifts_per_day': 3,
            'nurses_per_shift': 2,
            'expected': [
                [{'Alice', 'Charlie'}, {'Diana', 'Bob'}, {'Alice', 'Charlie'}],
                [{'Eve', 'George'}, {'Hector', 'Felix'}, {'Diana', 'Bob'}],
                [{'Alice', 'Charlie'}, {'Eve', 'George'}, {'Hector', 'Felix'}],
                [{'Diana', 'Bob'}, {'Alice', 'Charlie'}, {'Eve', 'George'}],
                [{'Hector', 'Felix'}, {'Diana', 'Bob'}, {'Alice', 'Charlie'}],
                [{'Eve', 'George'}, {'Hector', 'Felix'}, {'Diana', 'Bob'}],
                [{'Alice', 'Charlie'}, {'Eve', 'George'}, {'Hector', 'Felix'}]
            ]
        }
    ),
])
def test_generate_schedule(params):
    nurses = params['nurses']
    days = params['days']
    shifts_per_day = params['shifts_per_day']
    nurses_per_shift = params['nurses_per_shift']
    expected = params['expected']
    s = Scheduler(nurses, days, shifts_per_day)
    s.generate_schedule(nurses_per_shift)
    result = s.get_schedule()
    assert result == expected, f'{result} != {expected}'
