# ### Problem Statement:
# A company wants to segment its customers based on their annual income and spending score.
# You are given a dataset of five customers with the following values:
#
# | Customer | Annual Income ($1000s) | Spending Score (1-100) |
# |----------|-----------------|------------------|
# | 1        | 15              | 39               |
# | 2        | 45              | 81               |
# | 3        | 34              | 56               |
# | 4        | 60              | 10               |
# | 5        | 78              | 90               |
#
# Use **K-Means clustering (K=2)** to group these customers into two clusters.

def euclidean_distance(p1, p2):
    return sum((p1[i] - p2[i]) ** 2 for i in range(len(p1))) ** 0.5


def k_means(data, k, max_iters=10):
    centroids = data[:k]  # Initialize centroids as the first k points
    clusters = [[] for _ in range(k)]

    for _ in range(max_iters):
        clusters = [[] for _ in range(k)]

        # Assign each point to the nearest centroid
        for point in data:
            distances = [euclidean_distance(point, centroid) for centroid in centroids]
            cluster_index = distances.index(min(distances))
            clusters[cluster_index].append(point)

        # Recalculate centroids
        new_centroids = []
        for cluster in clusters:
            if cluster:
                new_centroid = [sum(dim) / len(cluster) for dim in zip(*cluster)]
                new_centroids.append(new_centroid)
            else:
                new_centroids.append(centroids[len(new_centroids)])

        if new_centroids == centroids:
            break
        centroids = new_centroids

    return clusters, centroids


# Dataset
customers = [
    [15, 39],
    [45, 81],
    [34, 56],
    [60, 10],
    [78, 90]
]

# Run K-Means with k=2
clusters, centroids = k_means(customers, k=2)

# Output results
print("Clusters:")
for i, cluster in enumerate(clusters):
    print(f"Cluster {i + 1}: {cluster}")
print("Centroids:", [[round(c, 4) for c in centroid] for centroid in centroids])


# Output:
#
# Clusters:
# Cluster 1: [[15, 39], [34, 56], [60, 10]]
# Cluster 2: [[45, 81], [78, 90]]
# Centroids: [[36.3333, 35.0], [61.5, 85.5]]
