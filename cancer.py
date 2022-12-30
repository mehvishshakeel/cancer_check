from matplotlib import pyplot as plt
import numpy as np
import pandas as pd


df = pd.read_csv(r'data.csv')

print (df)

df.hist(bins=50, figsize=(15, 15))
plt.tight_layout()
plt.show()

print ('please enter in the details of ypur tumor \n')
radius = input('radius mean \n')
texture = input('texture mean \n')
perimeter = input('perimeter mean \n')
area = input('area mean \n')
smoothness = input('smoothness mean \n')
compactness = input('compactness mean \n')
concavity = input('concavity mean \n')
concave_points = input('concave_points mean \n')


