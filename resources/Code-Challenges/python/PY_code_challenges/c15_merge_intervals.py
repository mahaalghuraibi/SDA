# -----------------------------------------------------------------
# Challenge: 15_merge_intervals
# Prompt:
# You are given a list of intervals represented as pairs [start, end].  
# Write a function called `merge_intervals` that merges all overlapping intervals 
# and returns a new list of non-overlapping intervals sorted by start time.
#
# Example input:
# intervals = [[1,3],[2,6],[8,10],[15,18]]
#
# Example function call:
# merge_intervals(intervals)
#
# Expected output:
# [[1,6],[8,10],[15,18]]
#
# Another example:
# intervals = [[1,4],[4,5]]
# merge_intervals(intervals)
# Expected output:
# [[1,5]]
#
# Constraints:
# - Intervals are represented as lists of two integers [start, end].
# - Intervals may be in any order.
# - Start is always less than or equal to end.
# -----------------------------------------------------------------
# -----------------------------------------------------------------
# Challenge: 15_merge_intervals
# -----------------------------------------------------------------

def merge_intervals(intervals):
    if not intervals or len(intervals) == 1:
        return intervals

    intervals.sort(key=lambda x: x[0])

    merged = []

    for interval in intervals:
        current_start = interval[0]
        current_end   = interval[1]

       
        if not merged:
            merged.append([current_start, current_end])
            continue

       
        last_start, last_end = merged[-1]

        
        if current_start <= last_end:
       
            merged[-1][1] = max(last_end, current_end)
        else:
        
            merged.append([current_start, current_end])


    return merged




print(merge_intervals([[1,4],[4,5]]))   
