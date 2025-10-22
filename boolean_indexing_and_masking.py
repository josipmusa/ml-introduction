import numpy as np

def boolean_indexing_and_masking():
    rng = np.random.default_rng()
    scores = rng.integers(low=0, high=101, size=100)
    print(scores)
    greater_than_seventy_mask = scores >= 70
    between_fifty_and_eighty_mask = (scores >= 50) & (scores <= 80)

    print("Over 70 scores count : ", np.sum(greater_than_seventy_mask))
    print("Between 50 and 80 scores count : ", np.sum(between_fifty_and_eighty_mask))
    scores[scores < 50] = 50
    print(scores)

if __name__ == '__main__':
    boolean_indexing_and_masking()