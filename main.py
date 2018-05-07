import pandas as pd
import numpy as np

food = pd.read_csv('en.openfoodfacts.org.products', sep='\t')
food.shape 
food.shape[0]
print food.shape 
print food.shape[1]

food.columns[103]