# Class Marks Analyzer

**PS No. 19** | B.Tech Computer Science and Engineering, First Semester

A Python 3 program that takes the marks of a class, validates them and uses NumPy to calculate basic statistics.

## Problem Statement

Create a program that takes the marks of a class as a list, validates them and uses NumPy to calculate the mean, median, highest, lowest, standard deviation, pass count and the number of students above average.

- Marks are entered as numbers separated by spaces.
- Marks must be from 0 to 100.
- Pass mark is 40.
- Standard deviation is the population value (`np.std` default).

## Features

- Reads marks into a list and converts it to a NumPy array
- Validates input (numbers only, range 0 to 100) and asks again if invalid
- Calculates mean, median, maximum, minimum and standard deviation
- Counts passed and failed students and the pass percentage
- Counts students scoring above the class average
- Prints results in a neat format

## Requirements

- Python 3.8 or higher
- NumPy

```bash
pip install numpy
```

## How to Run

```bash
python class_marks_analyzer.py
```

Then enter the marks separated by spaces when prompted, for example `40 50 60 70 80`.

In VS Code, you can also open the file and click the Run button (top right).

## Program Structure

| Function | Purpose |
|---|---|
| `get_marks()` | Reads and validates the marks. Repeats until the input is valid. Returns a list. |
| `analyze_marks(marks)` | Converts the list to a NumPy array and calculates all statistics. Returns a dictionary. |
| `display_results(r)` | Prints the results in a neat format. |
| `main()` | Runs the three steps above in order. |

## Sample Runs

**Test Case 1: Normal input**
```
Marks: 40 50 60 70 80

Mean: 60.00 | Median: 60.00
Max: 80 | Min: 40 | Std Dev: 14.14
Passed: 5 of 5 | Failed: 0 | Pass percentage: 100.00%
Above average: 2 students
```

**Test Case 2: Boundary / minimum input**
```
Marks: 75

Mean: 75.00 | Median: 75.00
Max: 75 | Min: 75 | Std Dev: 0.00
Passed: 1 of 1 | Failed: 0 | Pass percentage: 100.00%
Above average: 0 students
```

**Test Case 3: Invalid input**
```
Marks: 50 abc 70
Invalid marks 'abc'. Enter numbers only.
Marks: 50 105 70
Marks must be between 0 and 100.
```

**Test Case 4: Different valid scenario**
```
Marks: 25 50 75 100

Mean: 62.50 | Median: 62.50
Max: 100 | Min: 25 | Std Dev: 27.95
Passed: 3 of 4 | Failed: 1 | Pass percentage: 75.00%
Above average: 2 students
```

## Concepts Used

NumPy, Lists, Functions, Statistics

## Source Code

`class_marks_analyzer.py`

```python
"""
PS 19 - Class Marks Analyzer
Reads class marks, validates them (numbers only, 0 to 100) and uses NumPy
to calculate mean, median, max, min, standard deviation, pass/fail counts
and the number of students above average.
"""

import numpy as np

PASS_MARK = 40


def get_marks():
    """Keep asking until valid marks are entered. Returns a list of floats."""
    while True:
        raw = input("Marks: ").split()

        if not raw:
            print("Please enter at least one mark.")
            continue

        marks = []
        valid = True

        # Check 1: numbers only
        for item in raw:
            try:
                marks.append(float(item))
            except ValueError:
                print(f"Invalid marks '{item}'. Enter numbers only.")
                valid = False
                break

        if not valid:
            continue

        # Check 2: range 0 to 100
        if any(m < 0 or m > 100 for m in marks):
            print("Marks must be between 0 and 100.")
            continue

        return marks


def analyze_marks(marks):
    """Use NumPy to compute all statistics. Returns a dictionary."""
    arr = np.array(marks)
    mean = np.mean(arr)

    passed = int(np.sum(arr >= PASS_MARK))
    total = len(arr)

    return {
        "mean": mean,
        "median": np.median(arr),
        "max": np.max(arr),
        "min": np.min(arr),
        "std": np.std(arr),  # population standard deviation (default)
        "total": total,
        "passed": passed,
        "failed": total - passed,
        "pass_pct": passed / total * 100,
        "above_avg": int(np.sum(arr > mean)),
    }


def display_results(r):
    """Print the results in a neat format."""
    print()
    print(f"Mean: {r['mean']:.2f} | Median: {r['median']:.2f}")
    print(f"Max: {r['max']:g} | Min: {r['min']:g} | Std Dev: {r['std']:.2f}")
    print(f"Passed: {r['passed']} of {r['total']} | Failed: {r['failed']} "
          f"| Pass percentage: {r['pass_pct']:.2f}%")
    print(f"Above average: {r['above_avg']} students")


def main():
    print("=== Class Marks Analyzer ===")
    print("Enter marks (0-100) separated by spaces.\n")
    marks = get_marks()
    results = analyze_marks(marks)
    display_results(results)


if __name__ == "__main__":
    main()
```

## Files

- `class_marks_analyzer.py`: the source code
- `README.md`: this documentation
