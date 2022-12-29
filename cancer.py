from matplotlib import pyplot as plt
import numpy as np
import pandas as pd


df = pd.read_csv(r'data.csv')

print (df)

df.hist(bins=50, figsize=(15, 15))
plt.tight_layout()
plt.show()

