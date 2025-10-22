import numpy as np

def simulate_data_for_ml():
    rng = np.random.default_rng()
    array = rng.random(size=(100,3))

    first_column_weight = 0.3
    second_column_weight = 0.5
    third_column_weight = 0.1
    noise_std = 0.05
    noise = rng.normal(loc=0, scale=noise_std, size=100)
    target_vector = first_column_weight * array[:, 0] + second_column_weight * array[:, 1] + third_column_weight * array[:, 2] + noise
    print(target_vector)

    first_column_correlation = np.corrcoef(array[:, 0], target_vector)[0,1]
    second_column_correlation = np.corrcoef(array[:, 1], target_vector)[0,1]
    third_column_correlation = np.corrcoef(array[:, 2], target_vector)[0,1]

    print(first_column_correlation)
    print(second_column_correlation)
    print(third_column_correlation)


if __name__ == '__main__':
    simulate_data_for_ml()