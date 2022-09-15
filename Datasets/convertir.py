import pandas as pd

results = pd.read_json('results.json', lines=True)
results.head()