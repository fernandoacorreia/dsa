# Matrix-based Nurse Scheduling.
# See https://en.wikipedia.org/wiki/Nurse_scheduling_problem

import numpy as np
from typing import List, Tuple

class Nurse:
    def __init__(self, name: str, skill_level: int):
        self.name = name
        self.skill_level = skill_level

class Scheduler:
    def __init__(self, nurses: List[Nurse], days: int, shifts_per_day: int):
        # Store arguments.
        self.nurses = nurses
        self.days = days
        self.shifts_per_day = shifts_per_day
        # Initialize internal fields.
        self.matrix = np.zeros((len(nurses), days * shifts_per_day), dtype=int)
        self.hours_worked = np.zeros(len(nurses), dtype=int)
        self.high_skill_bar = 3
        self.max_hours_week = 48

    def generate_schedule(self, nurses_per_shift: int):
        # Iterate through each day.
        for day in range(self.days):
            # Iterate through each shift in a day.
            for shift in range(self.shifts_per_day):
                assigned_nurses = 0  # Keep track of how many nurses were assigned to the shift.
                high_skill_assigned = False  # Keep track of whether at least one high skill nurse was assigned to the shift.

                # Assign one high skill nurse to the shift, if available.
                for i, nurse in enumerate(self.nurses):
                    if nurse.skill_level < self.high_skill_bar:
                        continue
                    if self._is_available(i, day, shift):
                        self._assign_shift(i, day, shift)
                        assigned_nurses += 1
                        high_skill_assigned = True
                        break

                # Assign lower skill nurses to the same shift.
                for i, nurse in enumerate(self.nurses):
                    if assigned_nurses >= nurses_per_shift:
                        break
                    if self._is_available(i, day, shift) and nurse.skill_level < self.high_skill_bar:
                        self._assign_shift(i, day, shift)
                        assigned_nurses += 1

                # Assign high skill nurses to the same shift if needed.
                for i, nurse in enumerate(self.nurses):
                    if assigned_nurses >= nurses_per_shift:
                        break
                    if self._is_available(i, day, shift) and nurse.skill_level >= self.high_skill_bar:
                        self._assign_shift(i, day, shift)
                        high_skill_assigned = True
                        assigned_nurses += 1

                if not high_skill_assigned:
                    print(f"Warning: no high skill nurse was available for day {day}, shift {shift}.")
                if assigned_nurses < nurses_per_shift:
                    print(f"Warning: {assigned_nurses } nurse(s) assigned for day {day}, shift {shift} but {nurses_per_shift} are required")

    def _is_available(self, nurse_index: int, day: int, shift: int) -> bool:
        shift_index = day * self.shifts_per_day + shift

        # Check if already assigned to this shift
        if self.matrix[nurse_index, shift_index] == 1:
            return False

        # Check maximum hours
        if self.hours_worked[nurse_index] >= self.max_hours_week:
            return False

        # Check for consecutive shifts
        if shift_index > 0 and self.matrix[nurse_index, shift_index - 1] == 1:
            return False

        # Check for at least 12 hours between shifts
        if shift_index >= self.shifts_per_day and np.sum(self.matrix[nurse_index, shift_index - self.shifts_per_day:shift_index]) > 0:
            return False

        return True

    def _assign_shift(self, nurse_index: int, day: int, shift: int):
        shift_index = day * self.shifts_per_day + shift
        self.matrix[nurse_index, shift_index] = 1
        self.hours_worked[nurse_index] += 8

    def get_schedule(self):
        # Create a days x shifts matrix with empty sets
        days_and_shifts = np.empty((self.days, self.shifts_per_day), dtype=object)
        for d in range(self.days):
            for s in range(self.shifts_per_day):
                days_and_shifts[d, s] = set()  # a unique, empty set on each cell

        # Add nurses to the sets on the days and shifts they are assigned to.
        for n, nurse in enumerate(self.nurses):
            for d in range(self.days):
                for s in range(self.shifts_per_day):
                    shift_index = d * self.shifts_per_day + s
                    if self.matrix[n, shift_index] == 1:
                        days_and_shifts[d, s].add(nurse.name)
        
        # Return days and shifts with nurses as a list of lists.
        return days_and_shifts.tolist()

    def print_schedule(self):
        for i, nurse in enumerate(self.nurses):
            shifts = ['|X' if shift else '|-' for shift in self.matrix[i]]
            print(f"{nurse.name:20} {''.join(shifts)}|")

if __name__ == "__main__":
    print("main")
