def max_meetings(start, end, names):
    # Step 1: Pair each meeting with (start, end, name)
    meetings = list(zip(start, end, names))
    
    # Step 2: Sort by end time
    meetings.sort(key=lambda x: x[1])
    
    selected = []
    last_end = -1
    
    # Step 3: Greedy selection
    for s, e, name in meetings:
        if s >= last_end:       # no overlap
            selected.append((name, s, e))
            last_end = e
    
    return selected


# Example usage
start = [1, 3, 0, 5, 8, 5]
end   = [3, 4, 6, 7, 9, 9]
names = ["M1", "M2", "M3", "M4", "M5", "M6"]

result = max_meetings(start, end, names)

print("Selected meetings:")
for m in result:
    print(f"{m[0]}: {m[1]}–{m[2]}")

print("Maximum number of meetings:", len(result))
