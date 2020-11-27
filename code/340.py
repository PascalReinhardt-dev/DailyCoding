# Good morning! Here's your coding interview problem for today.

# This problem was asked by Google.

# Given a set of points (x, y) on a 2D cartesian plane, find the two closest points. For example, given the points [(1, 1), (-1, -1), (3, 4), (6, 1), (-1, -6), (-4, -3)], return [(-1, -1), (1, 1)].

def getClosestPoints2D(points):
    smallestDistance = float("inf")
    closetPoints = []
    for apoint in points:
        for bpoint in points:
            distance = abs(apoint[0] - bpoint[0]) + abs(apoint[1] - bpoint[1])
            if distance < smallestDistance and apoint != bpoint:
                closetPoints = [apoint,bpoint]
                smallestDistance = distance


    return closetPoints


points = [(1, 1), (-1, -1), (3, 4), (6, 1), (-1, -6), (-4, -3)]

for point in getClosestPoints2D(points):
    print(str(point[0]) + "," + str(point[1]))