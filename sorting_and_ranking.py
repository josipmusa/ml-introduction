import numpy as np

def sorting_and_ranking():
    rng = np.random.default_rng()
    numbers = rng.integers(low=0, high=100, size=50)
    print(numbers)
    top_5_indices = np.argpartition(numbers, -5)[-5:]
    print("Top 5 indices:", top_5_indices)

    sorted_numbers_desc = np.sort(numbers)[::-1]
    print("Sorted numbers:", sorted_numbers_desc)

    sorted_indices_asc = np.argsort(numbers)
    ranks = np.empty_like(numbers, dtype=int)
    ranks[sorted_indices_asc] = np.arange(1, len(numbers) + 1)
    percentiles = ranks / 50 * 100
    print("Percentiles:", percentiles)

if __name__ == '__main__':
    sorting_and_ranking()

