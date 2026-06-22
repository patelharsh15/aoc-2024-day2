"""
Advent of Code 2024 — Day 2: Red-Nosed Reports
================================================
Problem : https://adventofcode.com/2024/day/2

A report (line of space-separated integers) is **safe** when:
  1. Levels are strictly monotonic (all increasing OR all decreasing).
  2. Adjacent level differences ∈ [1, 3].

Part 1 — count reports that are safe as-is.
Part 2 — count reports safe under the *Problem Dampener*:
          a report is also safe if removing any single level makes it safe.

Complexity: O(N·K) per part-2 report where K = len(report), N = #reports.
"""

from __future__ import annotations

import sys
from pathlib import Path
from typing import Sequence


# ── Core predicates ──────────────────────────────────────────────────────────

def is_safe(levels: Sequence[int]) -> bool:
    """Return True if *levels* is strictly monotonic with diffs in [1, 3]."""
    diffs = [b - a for a, b in zip(levels, levels[1:])]
    return (
        all(1 <= d <= 3 for d in diffs)       # all increasing
        or all(-3 <= d <= -1 for d in diffs)   # all decreasing
    )


def is_safe_dampened(levels: Sequence[int]) -> bool:
    """Return True if *levels* is safe, or becomes safe after removing one element."""
    if is_safe(levels):
        return True
    return any(
        is_safe(levels[:i] + levels[i + 1:])
        for i in range(len(levels))
    )


# ── I/O & driver ─────────────────────────────────────────────────────────────

def parse(raw: str) -> list[list[int]]:
    """Parse multi-line input into a list of integer reports."""
    return [
        list(map(int, line.split()))
        for line in raw.strip().splitlines()
        if line.strip()
    ]


def solve(reports: list[list[int]]) -> tuple[int, int]:
    """Return (part1_answer, part2_answer)."""
    part1 = sum(is_safe(r) for r in reports)
    part2 = sum(is_safe_dampened(r) for r in reports)
    return part1, part2


def main() -> None:
    input_path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).parent / "input.txt"
    if not input_path.exists():
        sys.exit(f"Input file not found: {input_path}")

    reports = parse(input_path.read_text(encoding="utf-8"))
    part1, part2 = solve(reports)

    print(f"Part 1 — Safe reports          : {part1}")
    print(f"Part 2 — Safe (with dampener)  : {part2}")


if __name__ == "__main__":
    main()
