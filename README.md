# Advent of Code 2024 — Day 2: Red-Nosed Reports

Clean, production-grade Python solution.

## Problem

Determine how many "reports" (rows of integers) are **safe**:
- **Part 1** — levels must be strictly monotonic (all-increasing *or* all-decreasing) with adjacent differences in `[1, 3]`.
- **Part 2** — same rule, but the *Problem Dampener* lets you tolerate one bad level (remove any single element and re-check).

## Usage

```bash
# Run with your puzzle input
python solution.py input.txt

# Run tests
pytest test_solution.py -v
```

## Project Structure

| File                | Purpose                          |
|---------------------|----------------------------------|
| `solution.py`       | Main solver (Parts 1 & 2)       |
| `test_solution.py`  | Pytest suite with example data   |
| `input.txt`         | Your puzzle input (not tracked)  |

## Algorithm

| Function            | Complexity | Description                                  |
|---------------------|-----------|-----------------------------------------------|
| `is_safe`           | O(K)      | Single-pass diff check for monotonicity       |
| `is_safe_dampened`  | O(K²)     | Brute-force single-removal; sufficient for K≤~30 |
| `solve`             | O(N·K²)   | Iterates all N reports                        |

## License

MIT
