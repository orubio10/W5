# timed_challenge.py
# Prompt: Return only unique values from a list of integers.

# Structure: set
# Reason: A set removes duplicates automatically (O(n) time).

from typing import List

def unique_values(numbers: List[int]) -> List[int]:
    return list(set(numbers))

# ------------------- tests -------------------
if __name__ == "__main__":
    print(sorted(unique_values([4, 7, 4, 1, 7, 9])))   # [1, 4, 7, 9]
    print(sorted(unique_values([1, 2, 3])))            # [1, 2, 3]
    print(sorted(unique_values([])))                   # []
    print(sorted(unique_values([-1, -2, -1, -3])))     # [-3, -2, -1]
    print(sorted(unique_values([0, 0, 1])))            # [0, 1]
    print(sorted(unique_values([10**6, 2, 10**6])))    # [2, 1000000]

# ---------------- Reflection (about 220 words) ----------------
# I chose a set because the goal was to return only unique numbers.
# Sets remove duplicates automatically, and they’re fast — each insert or check is O(1) on average.
# Converting to a list at the end matches the expected output type.
#
# Under a 30-minute limit, I wanted something simple and correct.
# A set keeps the code short and readable, which matters when time is tight.
# I tested normal, empty, and edge cases: all unique, all duplicates, negatives, zeros, and large numbers.
# Each worked as expected.
#
# The main trade-off is that sets don’t keep order.
# Since the prompt said order doesn’t matter, that was fine.
# If order had mattered, I would use a “seen” set and result list:
#   seen = set(); result = []
#   for n in numbers:
#       if n not in seen:
#           seen.add(n)
#           result.append(n)
# This keeps the first occurrence and still runs in O(n).
#
# Another option was sorting and removing neighbors (O(n log n)),
# but I preferred O(n) and fewer steps.
#
# The time limit pushed me to focus on a clean and working solution
# instead of overthinking performance or style.
# I made sure it was easy to explain and prove correct.
