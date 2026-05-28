import pandas as pd
import numpy as np
import seaborn as sns
import os

df = pd.read_csv('https://raw.githubusercontent.com/araj2/customer-database/master/Ecommerce%20Customers.csv')
df = df.iloc[:,3:]

df.to_csv(os.path.join('data','customer.csv'))