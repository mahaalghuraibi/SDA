# -----------------------------------------------------------------
# Challenge: 19_sum_combinations
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
# sum_combinations([2,3,5], 8) -> [[3,5]]  # Each number used once
# sum_combinations([2,4,6], 6) -> [[6], [2,4]]
#
# Hints:
# - Consider using recursion/backtracking to explore combinations.
# - Make sure to check the current sum at each step and prune paths that exceed the target.
# -----------------------------------------------------------------

def sum_combinations(numbers, target):
    numbers.sort()
    result = []

    def backtrack(start_index, current_combination, current_sum):
        if current_sum == target:
            result.append(list(current_combination))
            return

        if current_sum > target:
            return

        for i in range(start_index, len(numbers)):
            if i > start_index and numbers[i] == numbers[i-1]:
                continue

            current_combination.append(numbers[i])
            backtrack(i+1, current_combination, current_sum + numbers[i])
            current_combination.pop()

    backtrack(0, [], 0)
    return result


print(sum_combinations([2,3,6,7], 7))
print(sum_combinations([2,3,5], 8))
print(sum_combinations([2,4,6], 6))
