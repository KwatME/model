from numpy import absolute, where
from scipy.spatial.distance import correlation


def compute_correlation_distance(x, y):

    distance = correlation(x, y)

    return where(absolute(distance) < 1e-8, 0, distance)
