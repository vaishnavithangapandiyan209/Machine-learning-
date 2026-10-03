def find_s(training_data):
    """
    training_data: list of tuples
    Each tuple contains:
    (attributes..., target)

    Target:
    'Yes' -> positive example
    'No'  -> negative example
    """

    # Initialize hypothesis with the most specific values
    hypothesis = ['0'] * (len(training_data[0]) - 1)

    for example in training_data:
        attributes = example[:-1]
        target = example[-1]

        # Consider only positive examples
        if target == 'Yes':
            for i in range(len(attributes)):
                if hypothesis[i] == '0':
                    hypothesis[i] = attributes[i]
                elif hypothesis[i] != attributes[i]:
                    hypothesis[i] = '?'

    return hypothesis


# Training data
training_data = [
    ('Sunny', 'Warm', 'Normal', 'Strong', 'Warm', 'Same', 'Yes'),
    ('Sunny', 'Warm', 'High',    'Strong', 'Warm', 'Same', 'Yes'),
    ('Rainy', 'Cold', 'High',    'Strong', 'Warm', 'Change', 'No'),
    ('Sunny', 'Warm', 'High',    'Strong', 'Cool', 'Change', 'Yes')
]

# Apply FIND-S
hypothesis = find_s(training_data)

print("Most Specific Hypothesis:", hypothesis)
