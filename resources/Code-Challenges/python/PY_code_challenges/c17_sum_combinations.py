# -----------------------------------------------------------------
# Challenge: 17_sum_combinations
# Prompt:
# Write a function called `sum_combinations` that accepts two arguments:
# 1) A list of positive integers `numbers`
# 2) A target sum `target`
#
# The function should return a list of all unique combinations of numbers
# from the list that sum up to the target. Each number in the list may be
# used **once per combination**.
#
# Notes:
# - The order of numbers in a combination does not matter.
# - The order of combinations in the output list does not matter.
# - No duplicate combinations should be returned.
#
# Example function calls:
# sum_combinations([2,3,6,7], 7) -> [[7]]
# sum_combinations([2,3,5], 8) -> [[3,5], [2,3,3]]  # if duplicates allowed, otherwise [3,5]
# sum_combinations([2,4,6], 6) -> [[6], [2,4]]
#
# Hints:
# - Consider using recursion/backtracking to explore combinations.
# - Make sure to check the current sum at each step and prune paths that exceed the target.
# -----------------------------------------------------------------

def sum_combinations(numbers, target):
    nums = sorted(numbers)
    results = []
    path = []

    def backtrack(start_index, remaining):
        if remaining == 0:
            results.append(path.copy())
            return
        if remaining < 0:
            return
        prev = None
        for i in range(start_index, len(nums)):
            if prev is not None and nums[i] == prev:
                continue
            path.append(nums[i])
            backtrack(i + 1, remaining - nums[i])
            path.pop()
            prev = nums[i]

    backtrack(0, target)
    return results


if __name__ == "__main__":
    print(sum_combinations([2, 3, 6, 7], 7))
    print(sum_combinations([2, 3, 5], 8))
    print(sum_combinations([2, 4, 6], 6))
    print(sum_combinations([2, 2, 3, 3], 6))
    print(sum_combinations([1, 1, 2, 5, 6, 7, 10], 8))
