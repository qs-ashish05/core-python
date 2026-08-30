# %%
import pandas as pd
import numpy as np
# %%
df = pd.read_csv('./datasets/diabetes/data_for_lr.csv')
df.head()
# %%
x_total = df['x'].sum()
y_total = df['y'].sum()

x_avg = df['x'].mean()
y_avg = df['y'].mean()

print(f"X sum = {x_total}")
print(f"Y sum = {y_total}")
print(f"X avg = {x_avg}")
print(f"Y avg = {y_avg}")
# %%
# y = mx + c

# m = [n(sum of xy) - (sum of x)(sum of y) ] // n(sum of x sqr) - sqr(sum of x)

# c = (sum of y) - m (sum of x) // n
# %%
df['xy'] = df['x'] * df['y']
df.head(5)
# %%
df['x sqr'] = df['x']**2
df.head()
# %%
n = df.shape[0]
print(f'Number of rows = {n}')
# %%
# according to formula of linear regression

# m = [n(sum of xy) - (sum of x)(sum of y) ] // n(sum of x sqr) - sqr(sum of x)

sum_of_xy = df['xy'].sum()
sum_of_x_sqr = df['x sqr'].sum()


m = (n * (sum_of_xy) - (x_total * y_total) ) / ((n*sum_of_x_sqr) - x_total **2)
print(f'value of m = {m}')
# %%
# c = (sum of y) - m (sum of x) // n

c = (y_total - m*x_total) / n
print(f'value of c = {c}')
# %%
# y_pred = m*x + c

df['y_pred'] = m*df['x'] + c
df.head(5)
# %%
import matplotlib.pyplot as plt

plt.plot(df['x'], df['y'],
         color='blue', marker='o',
         markerfacecolor='red',
         markeredgecolor='red',)

plt.plot(df['x'], df['y_pred'],
         color='green', marker='o',
         markerfacecolor='yellow',
         markeredgecolor='yellow',)

plt.show()
# %% [markdown]
# - Checking the values of m and c using library for Linear regression
# %%
from sklearn.linear_model import LinearRegression

lr_model = LinearRegression()
# %%
# Independent variable (X)
X = df[['x']]

# Dependent variable (Y)
y = df['y']
# %%
# Train the model
lr_model.fit(X, y)
# %%
# y = y.dropna()
# %%
# lr_model.fit(X, y)


# Note: if we remove the nan value only from the y then we will get the following inconsitency and error -

#  Found input variables with inconsistent numbers of samples: [700, 699]

# hence we have to remove the entire row of the data
# %%
df = pd.read_csv(
    './datasets/diabetes/data_for_lr.csv', )
df.head()
# %%
x = df[['x']]
y = df['y']
# %%
nan_indices = y[y.isna()].index
# %%
nan_indices
# %%
df = df.drop(index=nan_indices)
# %%
df.describe()
# %%
df['x'].isna().count()
# %%
df['y'].isna().count()
# %%
lr_model.fit(x, y)
# %%
# Remove rows where target column contains NaN
df = df.dropna(subset=['y'])

# Now create X and y
X = df.drop('y', axis=1)
y = df['y']
# %%
print(x.isna().sum())
# %%
lr_model.fit(X, y)
# %%
print(lr_model.coef_)
print(lr_model.intercept_)
# %%
print(m)
print(c)
# %%
df['y_model'] = lr_model.predict(df[['x']])
# %%
df.head(5)
# %%
