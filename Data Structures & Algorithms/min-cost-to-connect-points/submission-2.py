class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        dist = [math.inf] * n
        dist[0] = 0
        not_visited = set(range(n))
        cost = 0
        while not_visited:
            idx = - 1
            mn = math.inf
            for x in not_visited:
                if dist[x] < mn:
                    mn = dist[x]
                    idx = x
            cost += mn
            not_visited.remove(idx)
            x1, y1 = points[idx]
            for x in not_visited:
                x2, y2 = points[x]
                d = abs(x1-x2) + abs(y1-y2)
                if d < dist[x]: dist[x] = d
        return cost