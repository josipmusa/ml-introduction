import numpy as np
import matplotlib.pyplot as plt


def linear_algebra_basics():
    weights = np.array([[1, 2, 3],
                        [4, 5, 6],
                        [7, 8, 9]])

    random_transformation_matrix = np.array([
        [-1, 3, -5],
        [2, 1, -4],
        [5, 1, 2]
    ])

    feature_vector = np.array([[1],
                               [2],
                               [3]])

    matrix_vector_product = weights @ feature_vector
    print("Matrix vector product is : ", matrix_vector_product)

    transposed_weights = np.transpose(weights)
    final_transformation = transposed_weights @ random_transformation_matrix
    print("Final transformation is : ", final_transformation)

    two_by_two_matrix = np.array([
        [4, -5],
        [-2, 1]
    ])

    two_by_two_matrix_determinant = np.linalg.det(two_by_two_matrix)

    print("Two-by-two matrix determinant is : ", two_by_two_matrix_determinant)
    if two_by_two_matrix_determinant != 0:
        two_by_two_matrix_inverse = np.linalg.inv(two_by_two_matrix)
        print("Two-by-two matrix inverse is : ", two_by_two_matrix_inverse)
    else:
        print("Two-by-two matrix does not have an inverse")

if __name__ == '__main__':
    linear_algebra_basics()