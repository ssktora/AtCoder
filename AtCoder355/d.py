def count_overlapping_intervals(intervals):
    events = []
    for i, (l, r) in enumerate(intervals):
        events.append((l, 'start', i))
        events.append((r, 'end', i))

    events.sort(key=lambda x: (x[0], x[1] == 'end'))

    active_intervals = set()
    overlap_count = 0
    print(events)
    for event in events:
        position, event_type, index = event
        print(active_intervals)
        print(overlap_count)
        if event_type == 'start':
            overlap_count += len(active_intervals)
            active_intervals.add(index)
        else:
            active_intervals.remove(index)

    return overlap_count

intervals = []
N = int(input())
for i in range(N):
    l,r = map(int, input().split())
    intervals.append((l,r))

print(count_overlapping_intervals(intervals))  