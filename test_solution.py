"""Unit tests for AoC 2024 Day 2 — Red-Nosed Reports."""

import pytest
from solution import is_safe, is_safe_dampened, parse, solve

# ── Example data from the puzzle statement ───────────────────────────────────

EXAMPLE_INPUT = """\
7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
"""

EXAMPLE_REPORTS = [
    [7, 6, 4, 2, 1],
    [1, 2, 7, 8, 9],
    [9, 7, 6, 2, 1],
    [1, 3, 2, 4, 5],
    [8, 6, 4, 4, 1],
    [1, 3, 6, 7, 9],
]


# ── Parsing ──────────────────────────────────────────────────────────────────

def test_parse():
    assert parse(EXAMPLE_INPUT) == EXAMPLE_REPORTS


# ── is_safe (Part 1 predicate) ───────────────────────────────────────────────

@pytest.mark.parametrize("levels, expected", [
    ([7, 6, 4, 2, 1], True),   # decreasing, diffs in [1,3]
    ([1, 2, 7, 8, 9], False),  # 2→7 diff = 5
    ([9, 7, 6, 2, 1], False),  # 6→2 diff = 4
    ([1, 3, 2, 4, 5], False),  # not monotonic
    ([8, 6, 4, 4, 1], False),  # 4→4 diff = 0
    ([1, 3, 6, 7, 9], True),   # increasing, diffs in [1,3]
])
def test_is_safe(levels, expected):
    assert is_safe(levels) is expected


# ── is_safe_dampened (Part 2 predicate) ──────────────────────────────────────

@pytest.mark.parametrize("levels, expected", [
    ([7, 6, 4, 2, 1], True),   # already safe
    ([1, 2, 7, 8, 9], False),  # no single removal fixes it
    ([9, 7, 6, 2, 1], False),  # no single removal fixes it
    ([1, 3, 2, 4, 5], True),   # remove 3 → [1, 2, 4, 5]
    ([8, 6, 4, 4, 1], True),   # remove one 4 → [8, 6, 4, 1]
    ([1, 3, 6, 7, 9], True),   # already safe
])
def test_is_safe_dampened(levels, expected):
    assert is_safe_dampened(levels) is expected


# ── End-to-end solve ─────────────────────────────────────────────────────────

def test_solve_example():
    reports = parse(EXAMPLE_INPUT)
    part1, part2 = solve(reports)
    assert part1 == 2
    assert part2 == 4


# ── Edge cases ───────────────────────────────────────────────────────────────

def test_two_element_report():
    assert is_safe([1, 3]) is True
    assert is_safe([5, 5]) is False

def test_single_element_report():
    assert is_safe([42]) is True  # trivially monotonic

def test_dampener_removes_first():
    # [10, 1, 2, 3] — remove 10 → safe
    assert is_safe_dampened([10, 1, 2, 3]) is True

def test_dampener_removes_last():
    # [1, 2, 3, 99] — remove 99 → safe
    assert is_safe_dampened([1, 2, 3, 99]) is True
