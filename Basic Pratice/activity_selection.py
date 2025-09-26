def activity_selection(start,end):
    # Pair activities with start and end times
    activities = list(zip(start, end))

    # Sort activities by their end time
    activities.sort(key=lambda x: x[1])

    # to store chosen activities
    selected = [] 

    # initially, no activity has finished
    last_end_time = -1 
    
    # go through each activity
    for s, e in activities: 
        if s>=last_end_time:  # if it starts AFTER previous ended
            selected.append((s,e))  # choose it
            last_end_time = e # update last end time
    return selected

# Example usage
start = [1, 3, 0, 5, 8, 5]
end   = [2, 4, 6, 7, 9, 9]

result = activity_selection(start, end)
print("Selected activities (start, end):", result)
print("Maximum number of activities:", len(result))
