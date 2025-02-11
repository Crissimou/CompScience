# **Problem Statement**
# You are given a dataset of students' study hours and their exam results (Pass/Fail).
# Your task is to classify a new student based on their study hours using the **K-Nearest Neighbors (K-NN) algorithm** (with `k=3`).
#
# **Dataset**
# | Study Hours | Result  |
# |------------|---------|
# | 1.5        | Fail    |
# | 2.0        | Fail    |
# | 2.5        | Fail    |
# | 3.0        | Pass    |
# | 3.5        | Pass    |
# | 4.0        | Pass    |
#
# Given a new student who studied for **2.8 hours**, determine whether they will **Pass** or **Fail** using the K-NN algorithm.


def euclidean_distance(a, b):
    return abs(a - b)  # Since we have only one feature (study hours)


def knn_classify(data, new_point, k):
    # Compute distances
    distances = []
    for point, label in data:
        distance = euclidean_distance(point, new_point)
        distances.append((distance, label))

    # Sort by distance and pick k nearest neighbors
    distances.sort()  # Sorts based on the first element (distance)
    k_nearest = distances[:k]

    # Count occurrences of each class
    class_count = {}
    for _, label in k_nearest:
        if label in class_count:
            class_count[label] += 1
        else:
            class_count[label] = 1

    # Return the majority class
    return max(class_count, key=class_count.get)


# Dataset: (Study Hours, Result)
dataset = [(1.5, "Fail"), (2.0, "Fail"), (2.5, "Fail"),
           (3.0, "Pass"), (3.5, "Pass"), (4.0, "Pass")]

# New student with 2.8 hours of study
new_study_hours = 2.8
k = 3

prediction = knn_classify(dataset, new_study_hours, k)
print("Predicted result:", prediction)


# Output:
# Predicted result: Pass