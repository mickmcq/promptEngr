#!/usr/bin/env python3
"""
Assign presenters from names.txt to weeks 3-12.
Constraints:
- Everyone presents exactly once
- No more than 2 presenters per week
- At least 1 presenter per week
- No two consecutive weeks can have 2 presenters
"""

import random


def read_names(filename):
    """Read names from file, filtering out empty lines."""
    with open(filename, 'r') as f:
        names = [line.strip() for line in f if line.strip()]
    return names


def assign_presenters(names, start_week=3, end_week=12, randomize=True):
    """
    Assign presenters to weeks.

    Args:
        names: List of presenter names
        start_week: First week number (default 3)
        end_week: Last week number (default 12)
        randomize: Whether to shuffle names before assignment (default True)

    Returns:
        Dictionary mapping week numbers to list of presenters
    """
    # Create a copy of names to avoid modifying original
    presenter_list = names.copy()

    if randomize:
        random.shuffle(presenter_list)

    num_weeks = end_week - start_week + 1
    num_presenters = len(presenter_list)

    # Check if constraints can be satisfied
    if num_presenters > num_weeks * 2:
        raise ValueError(f"Too many presenters ({num_presenters}) for {num_weeks} weeks (max {num_weeks * 2})")
    if num_presenters < num_weeks:
        raise ValueError(f"Not enough presenters ({num_presenters}) for {num_weeks} weeks (min {num_weeks})")

    # Calculate how many weeks need 2 presenters
    weeks_with_two = num_presenters - num_weeks

    # Check if we can satisfy the no-consecutive constraint
    # Maximum weeks with 2 presenters without consecutive = ceil(num_weeks / 2)
    max_weeks_with_two = (num_weeks + 1) // 2
    if weeks_with_two > max_weeks_with_two:
        raise ValueError(f"Cannot satisfy constraint: need {weeks_with_two} weeks with 2 presenters, "
                        f"but can only have {max_weeks_with_two} without consecutive weeks")

    # Create a pattern: determine which weeks get 2 presenters
    # Strategy: spread them out evenly to avoid consecutive weeks
    weeks_list = list(range(start_week, end_week + 1))

    # Calculate spacing to distribute weeks with 2 presenters
    # We want to select weeks_with_two weeks from num_weeks, ensuring no two are consecutive
    two_presenter_weeks = set()

    if weeks_with_two > 0:
        # Use a greedy approach: space them as evenly as possible
        # Gap between weeks with 2 presenters should be at least 2
        gap = num_weeks // weeks_with_two
        if gap < 2:
            gap = 2  # Minimum gap to prevent consecutive

        # Start from a random offset
        offset = random.randint(0, min(gap - 1, num_weeks - weeks_with_two * 2))

        for i in range(weeks_with_two):
            week_idx = offset + i * gap
            if week_idx < num_weeks:
                two_presenter_weeks.add(weeks_list[week_idx])

    # Distribute presenters according to the pattern
    schedule = {}
    presenter_idx = 0

    for week in weeks_list:
        num_presenters_this_week = 2 if week in two_presenter_weeks else 1
        schedule[week] = []

        for _ in range(num_presenters_this_week):
            if presenter_idx < len(presenter_list):
                schedule[week].append(presenter_list[presenter_idx])
                presenter_idx += 1

    return schedule


def print_schedule(schedule):
    """Print the presentation schedule as a markdown table."""
    print("\n| Week | Presenter(s) |")
    print("|------|--------------|")
    for week in sorted(schedule.keys()):
        presenters = ", ".join(schedule[week])
        print(f"| {week:>4} | {presenters} |")


def main():
    # Read names from file
    names = read_names('names.txt')

    # Assign presenters to weeks
    schedule = assign_presenters(names, start_week=3, end_week=12, randomize=True)

    # Print the schedule as markdown table
    print_schedule(schedule)


if __name__ == "__main__":
    main()
