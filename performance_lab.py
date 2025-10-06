# 🔍 Problem 1: Find Most Frequent Element
# Given a list of integers, return the value that appears most frequently.
# If there's a tie, return any of the most frequent.
#
# Example:
# Input: [1, 3, 2, 3, 4, 1, 3]
# Output: 3

def most_frequent(numbers):
    from collections import Counter
    if not numbers:
        return None
    counts = Counter(numbers)
    return max(counts, key=counts.get)


"""
Time and Space Analysis for problem 1:
- Best-case: O(1) - If list has 0 or 1 elements.
- Worst-case: O(n) - Must count all elements in the list.
- Average-case: O(n) - Must traverse all elements once
- Space complexity: O(k) - k = number of unique elements
- Why this approach? Using a set gives O(1) average-time membership checks.
- Could it be optimized? - Not meaningfully—requires tracking seen items to preserve order.
"""


# 🔍 Problem 2: Remove Duplicates While Preserving Order
# Write a function that returns a list with duplicates removed but preserves order.
#
# Example:
# Input: [4, 5, 4, 6, 5, 7]
# Output: [4, 5, 6, 7]


def remove_duplicates(nums):
    seen = set()
    result = []
    for n in nums:
        if n not in seen:
            seen.add(n)
            result.append(n)
    return result

# Optimized Problem 2:
def remove_duplicates_optimized(nums):
    return list(dict.fromkeys(nums))


"""
Time and Space Analysis for problem 2:
- Best-case: O(n) → Need to iterate through list once.
- Worst-case: O(n) → Same as best; each element checked once.
- Average-case: O(n)
- Space complexity: O(n) for storing unique elements in the set and result list.
- Why this approach? Using a set gives O(1) average-time membership checks.
- Could it be optimized? Not meaningfully—requires tracking seen items to preserve order.
"""

"""
Time and Space Analysis for optimized problem 2: 
- Time Complexity: O(n) — single pass internally through the iterable
- Space Complexity: O(n) — stores keys only once
- Performance: Slightly faster in practice due to C-level dict implementation.
- Trade-off: Less explicit about what’s happening (relies on dict behavior).
- Why it’s better: Reduces Python-level loops and simplifies code.
"""

# 🔍 Problem 3: Return All Pairs That Sum to Target
# Write a function that returns all unique pairs of numbers in the list that sum to a target.
# Order of output does not matter. Assume input list has no duplicates.
#
# Example:
# Input: ([1, 2, 3, 4], target=5)
# Output: [(1, 4), (2, 3)]

def find_pairs(nums, target):
    seen = set()
    pairs = []
    for n in nums:
        complement = target - n
        if complement in seen:
            pairs.append((complement, n))
        seen.add(n)
    return pairs

"""
Time and Space Analysis for problem 3:
- Best-case: O(1) → If list is empty or has fewer than 2 elements.
- Worst-case: O(n) → Must check each element once.
- Average-case: O(n)
- Space complexity: O(n) for storing seen elements and output pairs.
- Why this approach? Single-pass solution with O(1) average lookup per element.
- Could it be optimized? A nested loop would be O(n²); this is already optimal for unsorted input.
"""

# 🔍 Problem 4: Simulate List Resizing (Amortized Cost)
# Create a function that adds n elements to a list that has a fixed initial capacity.
# When the list reaches capacity, simulate doubling its size by creating a new list
# and copying all values over (simulate this with print statements).
#
# Example:
# add_n_items(6) → should print when resizing happens.

def add_n_items(n):
    capacity = 1
    size = 0
    arr = [None] * capacity

    for i in range(n):
        if size == capacity:
            print(f"Resizing from {capacity} to {capacity * 2}")
            capacity *= 2
            new_arr = [None] * capacity
            for j in range(size):
                new_arr[j] = arr[j]
            arr = new_arr
        arr[size] = i
        size += 1
    print(f"Final array (capacity {capacity}): {arr[:size]}")
    return arr[:size]

# ✅ Test cases
add_n_items(6)
add_n_items(1)

"""
Time and Space Analysis for problem 4:
- When do resizes happen? Whenever size == capacity (1→2→4→8→...).
- Worst-case for a single append: O(n) when resizing and copying all elements.
- Amortized time per append: O(1) because doubling ensures total copies ≈ 2n overall.
- Space complexity: O(n) for the array storage.
- Why does doubling reduce cost overall? Because each element is copied a constant number of times on average.
"""


# 🔍 Problem 5: Compute Running Totals
# Write a function that takes a list of numbers and returns a new list
# where each element is the sum of all elements up to that index.
#
# Example:
# Input: [1, 2, 3, 4]
# Output: [1, 3, 6, 10]
# Because: [1, 1+2, 1+2+3, 1+2+3+4]


def running_total(nums):
    total = 0
    result = []
    for n in nums:
        total += n
        result.append(total)
    return result

"""
Time and Space Analysis for problem 5:
- Best-case: O(n) → Must process each number once.
- Worst-case: O(n)
- Average-case: O(n)
- Space complexity: O(n) for storing the resulting list.
- Why this approach? Simple one-pass accumulation, constant-time per iteration.
- Could it be optimized? Only by modifying the input list in-place (saves O(n) space but mutates data).
"""
