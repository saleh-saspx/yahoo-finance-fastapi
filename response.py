import numpy as np

def clean_data(data):
    if isinstance(data, np.integer):
        return int(data)
    elif isinstance(data, dict):
        return {key: clean_data(value) for key, value in data.items()}
    elif isinstance(data, list):
        return [clean_data(item) for item in data]
    else:
        return data