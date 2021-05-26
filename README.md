# Algorithmic-challenge
Algorithmic challenge - Time range


Suppose you get a list of intervals, containing a start and end time, e.g. [[0, 300], [600,1200], [3500, 6000]]. 
You should implement a function which will merge those single
intervals based on a given threshold value. If the difference between the end and start point
of two intervals is less than the threshold value, you will merge those two intervals, otherwise
you will leave them as they are. In case the threshold value is the same as the difference,
you can freely decide what to do, it doesn’t matter for this exercise if you leave them or
merge them in that specific case.
Some examples:
result = merge_intervals([[0, 300], [600, 1200], [3500, 6000]], threshold=400)
print(result)
[[0, 1200], [3500, 6000]]
result = merge_intervals([[0, 300], [600, 1200], [3500, 6000]], threshold=100)
print(result)
[[0, 300], [600, 1200], [3500, 6000]]
result = merge_intervals([[0, 300], [600, 1200], [3500, 6000]], threshold=2500)
print(result)
[[0, 6000]]
