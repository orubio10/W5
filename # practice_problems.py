# practice_problems.py
# Week 5 – Practice Problems

from collections import Counter, deque

# ------------------------------------------------------------
# Problem 1: First non-repeating character
# Data structure: dictionary (Counter)
# Reason:
# A dictionary lets me count each character quickly (O(n)).
# Then one pass finds the first unique character.
def first_unique_char(s: str) -> int:
    counts = Counter(s)
    for i, ch in enumerate(s):
        if counts[ch] == 1:
            return i
    return -1

# ------------------------------------------------------------
# Problem 2: Balanced brackets
# Data structure: stack (list)
# Reason:
# A stack tracks opening brackets and removes them when closed.
# Each char is processed once (O(n) time, O(n) space).
def is_balanced(s: str) -> bool:
    pairs = {')': '(', ']': '[', '}': '{'}
    stack = []
    for ch in s:
        if ch in pairs.values():
            stack.append(ch)
        elif ch in pairs:
            if not stack or stack[-1] != pairs[ch]:
                return False
            stack.pop()
    return not stack

# ------------------------------------------------------------
# Problem 3: Help-desk queue
# Data structure: queue (deque)
# Reason:
# A queue fits "first-come, first-served" logic.
# deque allows O(1) enqueue and dequeue.
class HelpDeskQueue:
    def __init__(self):
        self._q = deque()

    def enqueue(self, customer):
        self._q.append(customer)

    def dequeue(self):
        if not self._q:
            raise IndexError("empty queue")
        return self._q.popleft()

    def peek(self):
        return self._q[0] if self._q else None

    def __len__(self):
        return len(self._q)

# ------------------------- quick tests ----------------------
if __name__ == "__main__":
    assert first_unique_char("leetcode") == 0
    assert first_unique_char("aabb") == -1
    assert first_unique_char("loveleetcode") == 2

    assert is_balanced("()[]{}") is True
    assert is_balanced("([{}])") is True
    assert is_balanced("(]") is False
    assert is_balanced("([)]") is False

    q = HelpDeskQueue()
    q.enqueue("A")
    q.enqueue("B")
    assert q.peek() == "A"
    assert q.dequeue() == "A"
    assert q.dequeue() == "B"
    try:
        q.dequeue()
    except IndexError:
        pass

    print(" All practice problems passed.")
