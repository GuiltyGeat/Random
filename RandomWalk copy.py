import numpy as np
import matplotlib.pyplot as plt


def random_walk(n):
    coordinates = np.array([0, 0])
    path = [
        [0, 0]
        ]
    for i in range(n):
        step = np.random.random()
        if 0 <= step < 1/8: #step forward
            coordinates = coordinates + np.array([0, 1]) 
        elif 1/8 <= step < 2/8: #step back
            coordinates = coordinates + np.array([0, -1])
        elif 2/8 <= step < 3/8: #step right
            coordinates = coordinates + np.array([1, 0])
        elif 3/8 <= step < 4/8: #step left
            coordinates = coordinates + np.array([-1, 0])
        elif 4/8 <= step < 5/8: #step NE
            coordinates = coordinates + np.array([np.sqrt(1/2), np.sqrt(1/2)])
        elif 5/8 <= step < 6/8: #step NW
            coordinates = coordinates + np.array([-np.sqrt(1/2), np.sqrt(1/2)])
        elif 6/8 <= step < 7/8: #step SW
            coordinates = coordinates + np.array([-np.sqrt(1/2), -np.sqrt(1/2)])
        else: #step SE
            coordinates = coordinates + np.array([np.sqrt(1/2), -np.sqrt(1/2)])
        path = path + [list(coordinates)]
        distance = np.sqrt(np.sum(coordinates**2))
    return np.array(path)


def walk_dist(steps):
    coordinates = np.array([0, 0])
    path = [
        [0, 0]
        ]
    for i in range(steps):
        step = np.random.random()
        if 0 <= step < 1/8: #step forward
            coordinates = coordinates + np.array([0, 1]) 
        elif 1/8 <= step < 2/8: #step back
            coordinates = coordinates + np.array([0, -1])
        elif 2/8 <= step < 3/8: #step right
            coordinates = coordinates + np.array([1, 0])
        elif 3/8 <= step < 4/8: #step left
            coordinates = coordinates + np.array([-1, 0])
        elif 4/8 <= step < 5/8: #step NE
            coordinates = coordinates + np.array([np.sqrt(.5), np.sqrt(.5)])
        elif 5/8 <= step < 6/8: #step NW
            coordinates = coordinates + np.array([-np.sqrt(.5), np.sqrt(.5)])
        elif 6/8 <= step < 7/8: #step SW
            coordinates = coordinates + np.array([-np.sqrt(.5), -np.sqrt(.5)])
        else: #step SE
            coordinates = coordinates + np.array([np.sqrt(.5), -np.sqrt(.5)])
        path = path + [list(coordinates)]
        distance = np.sqrt(np.sum(coordinates**2))
    return np.array(distance)

def walk_coord(steps):
    coordinates = np.array([0, 0])
    for i in range(steps):
        step = np.random.random()
        if 0 <= step < 1/8: #step forward
            coordinates = coordinates + np.array([0, 1]) 
        elif 1/8 <= step < 2/8: #step back
            coordinates = coordinates + np.array([0, -1])
        elif 2/8 <= step < 3/8: #step right
            coordinates = coordinates + np.array([1, 0])
        elif 3/8 <= step < 4/8: #step left
            coordinates = coordinates + np.array([-1, 0])
        elif 4/8 <= step < 5/8: #step NE
            coordinates = coordinates + np.array([np.sqrt(.5), np.sqrt(.5)])
        elif 5/8 <= step < 6/8: #step NW
            coordinates = coordinates + np.array([-np.sqrt(.5), np.sqrt(.5)])
        elif 6/8 <= step < 7/8: #step SW
            coordinates = coordinates + np.array([-np.sqrt(.5), -np.sqrt(.5)])
        else: #step SE
            coordinates = coordinates + np.array([np.sqrt(.5), -np.sqrt(.5)])
    return coordinates

    
def final_coords(trials, steps):
    x = []
    for i in range(trials):
        x.append(walk_coord(steps))
    return np.array(x)


data = final_coords(1000, 400)

plt.hist(data)


def average_walk_dist(trials, steps):
    total = 0
    for i in range(trials):
        total = total + walk_dist(steps)
    return total/trials
def walk_dist_data(trials, steps):
    x = []
    for i in range(trials):
        x.append(float(walk_dist(steps)))
    return np.array(x)


data1 = random_walk(400)

x, y = data1.T

plt.title('Random Walking Path')
plt.plot(x, y, ls= '--')
plt.show()

data = walk_dist_data(1000, 400)
print(f'{average_walk_dist(1000, 400)} steps is the average final distance from the origin for a random walk of 400 steps')

plt.hist(data1)
plt.show()