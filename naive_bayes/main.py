# Sample training data
training_data = [
    ("Sunny", "Hot", "High", "Weak", "No"),
    ("Sunny", "Hot", "High", "Strong", "No"),
    ("Overcast", "Hot", "High", "Weak", "Yes"),
    ("Rain", "Mild", "High", "Weak", "Yes"),
    ("Rain", "Cool", "Normal", "Weak", "Yes"),
    ("Rain", "Cool", "Normal", "Strong", "No"),
    ("Overcast", "Cool", "Normal", "Strong", "Yes"),
    ("Sunny", "Mild", "High", "Weak", "No"),
    ("Sunny", "Cool", "Normal", "Weak", "Yes"),
    ("Rain", "Mild", "Normal", "Weak", "Yes"),
    ("Sunny", "Mild", "Normal", "Strong", "Yes"),
    ("Overcast", "Mild", "High", "Strong", "Yes"),
    ("Overcast", "Hot", "Normal", "Weak", "Yes"),
    ("Rain", "Mild", "High", "Strong", "No")
]


# Function to calculate probability
def calculate_probability(data, feature_index, feature_value, target_value):
    count_feature_target = 0
    count_target = 0

    for row in data:
        if row[-1] == target_value:
            count_target += 1
            if row[feature_index] == feature_value:
                count_feature_target += 1

    return (count_feature_target / count_target * 100) if count_target != 0 else 0


# Function to predict class
def predict(data, features):
    target_values = list(set(row[-1] for row in data))
    probabilities = {}

    for target in target_values:
        target_prob = sum(1 for row in data if row[-1] == target) / len(data)
        conditional_prob = 1

        for i in range(len(features)):
            conditional_prob *= calculate_probability(data, i, features[i], target) / 100

        probabilities[target] = round(target_prob * conditional_prob * 100, 4)

    return max(probabilities, key=probabilities.get), probabilities


# Example prediction
new_data = ("Rain", "Mild", "Normal", "Weak")
result, probs = predict(training_data, new_data)
print(f"Predicted class: {result} with probabilities: {probs}")
