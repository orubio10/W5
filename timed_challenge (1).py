# timed_challenge.py
# Paste of chosen prompt (as a comment):
# Prompt: Write a function that returns only the unique values from a list of integers.
# The order does not matter, but duplicates should be removed.

# Structure chosen: set
# Reason (short): A set stores unique values by definition and supports O(1) average insert/membership,
# so converting the list to a set removes duplicates in linear time and simple code.

from typing import List

def unique_values(numbers: List[int]) -> List[int]:
    # Core logic (O(n) average time, O(n) space)
    return list(set(numbers))

# ------------------------- tests ----------------------------
# Order may vary because a set is unordered.
if __name__ == "__main__":
    print(sorted(unique_values([4, 7, 4, 1, 7, 9])))  # -> [1, 4, 7, 9]
    print(sorted(unique_values([1, 2, 3])))           # -> [1, 2, 3]
    print(sorted(unique_values([])))                  # -> []
    print(sorted(unique_values([-1, -2, -1, -3])))    # -> [-3, -2, -1]
    print(sorted(unique_values([0, 0, 1])))           # -> [0, 1]
    print(sorted(unique_values([10**6, 2, 10**6])))   # -> [2, 1000000]


# Reflection 
# I picked a set because uniqueness is the main requirement and order is irrelevant.
# A set removes duplicates naturally and makes membership checks average O(1).
# That gives me a clean, reliable solution in one line: list(set(nums)).
# Under a 30‑minute limit, I wanted a path with the fewest moving parts and the lowest risk of bugs.
#
# I started by writing a few tests that covered normal cases and edge cases: an empty list,
# all-unique input, negative numbers, zero duplicates, and very large integers.
# Those gave me quick feedback that the function met the goal.
# The most important trade‑off I accepted is that sets do not preserve order.
# The prompt explicitly said order doesn’t matter, so this trade‑off is acceptable.
# If order had mattered, I would have switched to a “seen” hash set plus a result list to keep
# the first appearance of each value while preserving input order:
#
#     seen = set(); out = []
#     for x in nums:
#         if x not in seen: seen.add(x); out.append(x)
#
# That variant is still O(n) and keeps order deterministically.
# Another alternative is sorting then removing adjacent duplicates, which is simple but O(n log n).
# I avoided that because O(n) is better and sorting changes the original order anyway.
#
# Overall, the time box shaped my decision to prioritize a correct, readable O(n) solution
# that matches the problem’s constraints. I justified the data structure choice (set),
# implemented the core logic, and validated with tests that mirror the edge cases I’d expect in an interview.
