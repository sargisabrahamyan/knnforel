
import numpy as np
import math
import random
import os
import dataretriver

# Gets the neighbour points of the given point by given distance
def getNeighbours(p, r, points):
    neighbours = set(tuple())
    for point in points:
        distance = math.sqrt(pow(point[0] - p[0], 2) + pow(point[1] - p[1], 2))
        if distance <= r:
            #print("Distance beetwen ", point, "and", p, "is", distance)
            neighbours.add(point)

    return neighbours

# Center the given points to one point and return it
def centerPoints(points):
    if len(points) == 0:
        return None
    sum_x = 0
    sum_y = 0
    for point in points:
        sum_x += point[0]
        sum_y += point[1]
    x = sum_x / len(points)
    y = sum_y / len(points)
    return (x, y)

def getRandomPoint(points):
    randompoints = random.sample(points, 1)
    # first random point
    return randompoints[0]

def is_clusterisation_completed(points):
    return len(points) == 0

def delete_points(subpoints, points):
    for point in subpoints:
        try:
            points.remove(point)
        except ValueError:
            pass

def forel(radius, points):
    print("Number of points - ", len(points))
    print("Radius - ", radius)
    clusters = set(tuple())
    while not is_clusterisation_completed(points):
        current_point = getRandomPoint(points)
        neghtboors = getNeighbours(current_point, radius, points)
        center_point = centerPoints(neghtboors)
        while current_point != center_point:
            current_point = center_point
            neghtboors = getNeighbours(current_point, radius, points)
            center_point = centerPoints(neghtboors)
        delete_points(neghtboors, points)
        # we found a cluster
        clusters.add(current_point)
    print("Number of clusters - ", len(clusters))
    print("Clusters - ", clusters)
    return clusters

def getOptimalRadius(points):
    return 10

points = set(tuple())
points.add((1, 2))
points.add((4, 6))

points = dataretriver.getPointsFromCanvas(50, 100)
# OR
points = dataretriver.getPointsFromFile(os.path.join(os.getcwd(), "data.txt"))

print(points)

r = getOptimalRadius(points)

clusters = forel(r, points)
print(clusters)


