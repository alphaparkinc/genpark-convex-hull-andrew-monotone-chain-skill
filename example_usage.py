from client import ConvexHullMonotoneChain

points = [(0, 0), (1, 1), (2, 2), (0, 2), (2, 0), (1, 0.5), (0.5, 1.5)]
hull = ConvexHullMonotoneChain.compute_hull(points)
area = ConvexHullMonotoneChain.polygon_area(hull)
perim = ConvexHullMonotoneChain.polygon_perimeter(hull)

print("Convex Hull Vertices:", hull)
print(f"Area: {area:.4f} | Perimeter: {perim:.4f}")
