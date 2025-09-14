from typing import List

def merge_two_entries(a: List[int], b: List[int]) -> List[List[int]]:
    left, right = (a, b) if a[0] <= b[0] else (b, a)

    if left[1] >= right[0]:
        merged_end = max(left[1], right[1])
        return [[left[0], merged_end]]
    else:
        return [left, right]

def insert_interval(main: List[List[int]], to_insert: List[int]) -> List[List[int]]:
    results = []
    intervals = [to_insert] + main 
    intervals.sort(key=lambda x: x[0])

    results.append(intervals[0])

    for i in range(1, len(intervals)):
        arr1 = intervals[i]
        arr2 = results.pop() 
        merged = merge_two_entries(arr1, arr2)

        results.append(merged[0])
        if len(merged) == 2:
            results.append(merged[1])

    return results


main_intervals = [[1,3],[6,9]]
to_insert = [2,5]
print(insert_interval(main_intervals, to_insert))  # [[1, 5], [6, 9]]
