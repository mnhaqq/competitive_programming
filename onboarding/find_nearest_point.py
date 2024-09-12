from collections import OrderedDict

class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        store = [tuple(i) for i in points]
        manhattan_distances = []
        dic = OrderedDict()

        points = [point for point in points if point[0] == int(x) or point[1] == int(y)] 
        if len(points) == 0:
            return -1

        points = [tuple(i) for i in points]
        for point in points:
            manhattan_distances.append(abs(point[0]-x)+abs(point[1]-y))

        i = 0
        while i < len(points):
            dic[points[i]] = manhattan_distances[i]
            i+=1

        minimum = min(manhattan_distances)

        for key, value in dic.items():
            if value == minimum:
                nearest = key
                break

        return store.index(nearest)