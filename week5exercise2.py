import math
import itertools

def closest_distance(points):
    """
    Calculate the minimum Euclidean distance between any two points.
    
    Args:
        points (list of tuples): List of 2D points as (x, y) tuples.
    
    Returns:
        float: The minimum distance, rounded to 3 decimal places.
    """
    if len(points) < 2:
        return 0.0  
    
    min_dist = float('inf')
    for p1, p2 in itertools.combinations(points, 2):
        dist = math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)
        if dist < min_dist:
            min_dist = dist
    
    return round(min_dist, 3)


points = [(1, 2), (4, 6), (5, 5), (3, 3), (7, 8)]
print(closest_distance(points)) 