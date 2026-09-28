"""Andrew's Monotone Chain 2D Convex Hull Engine.
100% Python Standard Library.
"""

import math

class ConvexHullMonotoneChain:
    """Andrew's Monotone Chain 2D Convex Hull algorithm O(n log n)."""
    @staticmethod
    def cross_product(o, a, b):
        """2D cross product of OA and OB vectors. >0 for ccw turn, <0 for cw turn, 0 if collinear."""
        return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

    @classmethod
    def compute_hull(cls, points):
        pts = sorted(set(points))
        if len(pts) <= 1:
            return pts

        lower = []
        for p in pts:
            while len(lower) >= 2 and cls.cross_product(lower[-2], lower[-1], p) <= 0:
                lower.pop()
            lower.append(p)

        upper = []
        for p in reversed(pts):
            while len(upper) >= 2 and cls.cross_product(upper[-2], upper[-1], p) <= 0:
                upper.pop()
            upper.append(p)

        return lower[:-1] + upper[:-1]

    @staticmethod
    def polygon_area(hull):
        n = len(hull)
        if n < 3:
            return 0.0
        area = 0.0
        for i in range(n):
            j = (i + 1) % n
            area += hull[i][0] * hull[j][1] - hull[j][0] * hull[i][1]
        return abs(area) * 0.5

    @staticmethod
    def polygon_perimeter(hull):
        n = len(hull)
        if n < 2:
            return 0.0
        perim = 0.0
        for i in range(n):
            j = (i + 1) % n
            perim += math.hypot(hull[j][0] - hull[i][0], hull[j][1] - hull[i][1])
        return perim
