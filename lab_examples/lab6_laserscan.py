import numpy as np
import matplotlib.pyplot as plt

def max_obstacle_dist(laserscan, robot_width=0.1):

    readings = laserscan['readings']
    angles = np.linspace(laserscan['min_angle'], laserscan['max_angle'], readings.size)

    x_coords = np.cos(angles) * readings
    y_coords = np.sin(angles) * readings

    # Plotting for illustration
    plt.scatter(x_coords, y_coords)
    plt.xlim(0, 2)
    plt.savefig('robot.png')

    in_front_of_robot = np.abs(y_coords) < robot_width / 2
    if not in_front_of_robot.size:
        return np.inf
    else:
        return np.min(x_coords[in_front_of_robot])


def generate_laserscan_data():

    wall_far_dist = np.random.uniform(0.4, 1.5)
    wall_dist = np.random.uniform(0.2, 1.0)
    left_angle_cutoff = np.random.uniform(-np.pi/4, np.pi/4)
    wall_len = np.random.uniform(0, np.pi/8)

    angles = np.linspace(-np.pi/4, np.pi/4, 101)
    far_wall = (angles < left_angle_cutoff) | (angles > left_angle_cutoff + wall_len)
    rez = np.zeros(angles.shape)
    rez[far_wall] = wall_far_dist / np.cos(angles[far_wall])
    rez[~far_wall] = wall_dist / np.cos(angles[~far_wall])
    rez += np.random.normal(0, 0.02, size=rez.shape)

    return {
        'min_angle': -np.pi/4,
        'max_angle': np.pi/4,
        'readings': rez
    }


if __name__ == '__main__':

    data = generate_laserscan_data()
    dist = max_obstacle_dist(data, 0.1)
    print(dist)