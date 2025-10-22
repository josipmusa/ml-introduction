import numpy as np

def broadcasting_practice():
    rng = np.random.default_rng()
    matrix = rng.integers(low=0, high=5, size=(5, 5))
    print(matrix)

    row_mean = np.mean(matrix, axis=1, keepdims=True)
    print(row_mean)

    subtracted_matrix = matrix - row_mean
    print(subtracted_matrix)

    scalar = np.array([1, 2, 3, 4, 5])
    scaled_matrix = matrix * scalar
    print(scaled_matrix)

    bias_vector_for_columns = np.array([1, 2, 3, 4, 5])
    matrix_with_bias_added = matrix + bias_vector_for_columns
    print(matrix_with_bias_added)


if __name__ == '__main__':
     broadcasting_practice()