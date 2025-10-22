import numpy as np


def random_data_and_statistics():
    rng = np.random.default_rng()
    array = rng.random(size=1000)
    mean = np.mean(array)
    median = np.median(array)
    deviation = np.std(array)
    minimum = np.min(array)
    maximum = np.max(array)
    first_quarter_percentile_cutoff = np.percentile(array, 25)
    third_quarter_percentile_cutoff = np.percentile(array, 75)
    standardized_array = (array - mean) / deviation
    standardized_mean = np.mean(standardized_array)
    standardized_deviation = np.std(standardized_array)

    print("Mean: ", round(mean,2))
    print("Median: ", round(median,2))
    print("Deviation: ", round(deviation,2))
    print("Minimum: ", round(minimum, 2))
    print("Maximum: ", round(maximum, 2))
    print("25th percentile cutoff: ", round(first_quarter_percentile_cutoff, 2))
    print("75th percentile cutoff: ", round(third_quarter_percentile_cutoff, 2))
    print("Standardized mean: ", round(standardized_mean, 2))
    print("Standardized deviation: ", round(standardized_deviation, 2))


if __name__ == '__main__':
    random_data_and_statistics()