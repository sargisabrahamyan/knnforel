import matplotlib.pyplot as plt
import os

points = set(tuple())
board = plt.figure()
# Get points from canvas
def onclick(event):
    global points
    global board
    plt.plot(event.xdata, event.ydata, 'ro')
    points.add((int(event.xdata), int(event.ydata)))
    print(event.x, event.y)
    board.canvas.draw()

def getPointsFromCanvas(width, height):
    global points
    global board
    points = set(tuple())
    ax = board.add_subplot(111)
    ax.set_xlim([0, width])
    ax.set_ylim([0, height])
    cid = board.canvas.mpl_connect('button_press_event', onclick)
    plt.show()
    return points

def getPointsFromFile(path, splitter=" "):
    global points
    points = set(tuple())
    with open(path) as f:
        content = f.readlines()
        for line in content:
            print(line)
            pointStr = line.split(splitter)
            if pointStr != None and type(pointStr) and len(pointStr) == 2 :
                x_str = pointStr[0]
                y_str = pointStr[1]
                try:
                    x = int(x_str)
                    y = int(y_str)
                    points.add((x, y))
                except ValueError:
                    print("Avoid invalid input - ", line)
    return points


def showPoints(points, width, height) :
    board = plt.figure()
    ax = board.add_subplot(111)
    ax.set_xlim([0, width])
    ax.set_ylim([0, height])
    cid = board.canvas.mpl_connect('button_press_event', onclick)
    for point in points :
        plt.plot(point[0], point[1], 'ro')
    board.canvas.draw()
    plt.show()