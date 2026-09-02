# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# %%
df = pd.read_csv('./datasets/diabetes/data_for_lr.csv')
df.head()
# %%
print(df['y'].isna().sum())
print(df['x'].isna().sum())
# %%
df.shape
# %%
df = df.dropna(subset=['y'])
df.shape
# %%
print(df['y'].isna().sum())
print(df['x'].isna().sum())
# %%
df['xy'] = df['x'] * df['y']
df['x_sqr'] = df['x']**2
# %%
df.head(5)
# %%
# m = (n*sum_xy  - sum_x*sum_y) / n.sum_x2 - (sum_x)^2
# c = avg_y - (m/n)*avg_x
# %%
sum_xy = df['xy'].sum()
sum_x = df['x'].sum()
sum_y = df['y'].sum()
sum_x2 = df['x_sqr'].sum()

n = df.shape[0]
# %%
m = (n*sum_xy  - sum_x*sum_y) / n*sum_x2 - (sum_x)**2
# %%
avg_x = df['x'].mean()
avg_y = df['y'].mean()


c = avg_y - (m/n)*avg_x
# %%
print(f' m = {m}')
print(f' c = {c}')
# %% [markdown]
#     - Using sklearn library
# %%
from sklearn.linear_model import LinearRegression

model = LinearRegression()
# %%
x = df[['x']]
y = df['y']
# %%
model.fit(x,y)
# %%
print(f' m = {model.coef_}')
print(f' c = {model.intercept_}')
# %%
