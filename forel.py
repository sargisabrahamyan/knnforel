
import numpy as np
import math
import random
import os
import dataretriver

# Gets the neighbour points of the given point by given distance
def getNeighbours(p, r, points):
    neighbours = set(tuple())
    for point in points:
        distance = getDistance(p, point)
        if distance <= r:
            #print("Distance beetwen ", point, "and", p, "is", distance)
            neighbours.add(point)

    return neighbours

def getDistance(p1, p2) :
    return math.sqrt(pow(p1[0] - p2[0], 2) + pow(p1[1] - p2[1], 2))
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

def getOptimalRadius(points, algorithm="average"):
    points_list = list(points)
    if algorithm == "average":
        sum_dist = 0
        k = 0
        for i in range(0, len(points_list) - 1):
            for j in range(i + 1, len(points_list)):
                k = k + 1
                sum_dist = sum_dist + getDistance(points_list[i], points_list[j])
            i = i + 1
        return sum_dist / k
    return 10

points = set(tuple())
points.add((1, 2))
points.add((4, 6))

points = dataretriver.getPointsFromCanvas(50, 100)
# OR
#points = dataretriver.getPointsFromFile(os.path.join(os.getcwd(), "data.txt"))

print(points)

r = getOptimalRadius(points)
clusters = forel(r, points)
print(clusters)
dataretriver.showPoints(clusters, 50, 100)


