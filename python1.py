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