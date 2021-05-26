def time_range(intervals, threshold):

    result = []
    start = []
    for point in intervals:
        difference = point[1] - point[0]

        if difference >= threshold:
            result.append(point)
        else:
            start.append(point)

    if start:
        result[0][0] = start[0][0]
    return result


try:
    result1 = time_range([[0, 300], [600, 1200], [3500, 6000]], 400)
    result2 = time_range([[0, 300], [600, 1200], [3500, 6000]], 100)
    result3 = time_range([[0, 300], [600, 1200], [3500, 6000]], 2500)
    result4 = time_range([[2, 300], [600, 1200], [3500, 6000], [6000, 9000]], 2800)
    print(result1)
    print(result2)
    print(result3)
    print(result4)
except:
    print('threshold is too high')