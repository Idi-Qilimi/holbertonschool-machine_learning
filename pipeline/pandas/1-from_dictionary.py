import pandas as pd

data = {
    'First': [0.0, 0.5, 1.0, 1.5],
    'Second': ['one', 'two', 'three', 'four']
}

index_labels = ['A', 'B', 'C', 'D']

df = pd.DataFrame(data, index=index_labels)
