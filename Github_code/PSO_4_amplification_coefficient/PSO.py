import numpy as np
import scipy.io as sio
import differ_calculation

if __name__ == "__main__":
    # Initialize parameters
    # for defects abc
    differ_calculation.calculate_differ_abc()
    data = sio.loadmat('differ_abc.mat')
    summ = data['summ']
    # print(summ)

    num_particles = 50
    num_dimensions = 1
    max_iterations = 1000
    w = 0.15
    c1 = 2.0
    c2 = 2.0
    lower_bound = 1
    upper_bound = 30

    # Initialize particles and velocity
    particles = lower_bound + (upper_bound - lower_bound) * np.random.rand(num_particles, num_dimensions)
    velocities = np.zeros((num_particles, num_dimensions))

    # Initialize optimal result
    global_best_position = np.zeros((1, num_dimensions))
    global_best_fitness = np.inf
    score = np.zeros(1)

    n_c = 5
    mul = 1
    pic_num = 1

    # iteration
    for i in range(1, max_iterations + 1):

        # refresh position and velocity of each atom
        for j in range(num_particles):
            # calculate the optimal results
            mul = particles[j, :]
            score = 1 / (1 + min(summ) * mul) - 1 / (1 + max(summ) * mul)

            fitness = -np.sum(score)

            if fitness < global_best_fitness:
                global_best_fitness = fitness
                global_best_position = particles[j, :]

            # refresh velocity
            velocities[j, :] = w * velocities[j, :] + c1 * np.random.rand(1, num_dimensions) * (
                    particles[j, :] - global_best_position) + c2 * np.random.rand(1, num_dimensions) * (
                                       global_best_position - particles[j, :])

            # refresh position
            particles[j, :] = particles[j, :] + velocities[j, :]

            particles[j, :] = np.maximum(particles[j, :], lower_bound)
            particles[j, :] = np.minimum(particles[j, :], upper_bound)


    with open('output_amplification_coefficient.txt', 'w') as file:
        print('amplification_coefficient for split vacancy(a,b&c): \n', global_best_position, file=file)


    # for defects de
    differ_calculation.calculate_differ_de()
    data = sio.loadmat('differ_de.mat')
    summ = data['summ']
    # print(summ)

    num_particles = 50
    num_dimensions = 1
    max_iterations = 1000
    w = 0.15
    c1 = 2.0
    c2 = 2.0
    lower_bound = 1
    upper_bound = 30

    # Initialize particles and velocity
    particles = lower_bound + (upper_bound - lower_bound) * np.random.rand(num_particles, num_dimensions)
    velocities = np.zeros((num_particles, num_dimensions))

    # Initialize optimal result
    global_best_position = np.zeros((1, num_dimensions))
    global_best_fitness = np.inf
    score = np.zeros(1)

    n_c = 5
    mul = 1
    pic_num = 1

    # iteration
    for i in range(1, max_iterations + 1):

        # refresh position and velocity of each atom
        for j in range(num_particles):
            # calculate the optimal results
            mul = particles[j, :]
            score = 1 / (1 + min(summ) * mul) - 1 / (1 + max(summ) * mul)

            fitness = -np.sum(score)

            if fitness < global_best_fitness:
                global_best_fitness = fitness
                global_best_position = particles[j, :]

            # refresh velocity
            velocities[j, :] = w * velocities[j, :] + c1 * np.random.rand(1, num_dimensions) * (
                    particles[j, :] - global_best_position) + c2 * np.random.rand(1, num_dimensions) * (
                                       global_best_position - particles[j, :])

            # refresh position
            particles[j, :] = particles[j, :] + velocities[j, :]

            particles[j, :] = np.maximum(particles[j, :], lower_bound)
            particles[j, :] = np.minimum(particles[j, :], upper_bound)

    with open('output_amplification_coefficient.txt', 'a') as file:
        print('\namplification_coefficient for split interstitial(d&e): \n', global_best_position, file=file)
