# Advent of Code 2024 — Day 2: Red-Nosed Reports

My solution for [AoC 2024 Day 2](https://adventofcode.com/2024/day/2) in Python.

## Problem

Given a list of reports (rows of integers), figure out how many are **safe**.

- **Part 1** — A report is safe if the levels are strictly monotonic (all going up or all going down) and every adjacent pair differs by 1 to 3.
- **Part 2** — Same rules, but the *Problem Dampener* kicks in: a report counts as safe if removing any single level makes it pass the check.

## How to Run

```bash
# solve with the included example input
python solution.py input.txt

# run the test suite
pytest test_solution.py -v
```

## Files

| File              | What it does                     |
|-------------------|----------------------------------|
| `solution.py`     | Main solver for Parts 1 & 2     |
| `test_solution.py`| Pytest suite with example data   |
| `input.txt`       | Puzzle input                     |

## Quick Notes

- `is_safe(levels)` does a single-pass diff check — O(K).
- `is_safe_dampened(levels)` brute-forces single-element removal — O(K²), plenty fast for the input sizes here.
