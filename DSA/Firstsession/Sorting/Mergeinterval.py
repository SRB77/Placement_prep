# https://my.newtonschool.co/playground/code/mrnlnvc7vdsg  (Merged Interval)

def merge(intervals):
    # Step 1: Sort the intervals based on the start time
    intervals.sort(key=lambda x: x[0])
    
    # Step 2: Initialize a list to hold the merged intervals
    merged = []
    
    for interval in intervals:
        # If the merged list is empty or there is no overlap, add the interval
        if not merged or merged[-1][1] < interval[0]:
            merged.append(interval)
        else:
            # There is an overlap, so merge the current interval with the last one in merged
            merged[-1][1] = max(merged[-1][1], interval[1])
    
    return merged