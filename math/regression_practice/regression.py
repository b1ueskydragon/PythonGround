import pandas as pd
import matplotlib.pyplot as plt

# data frame
df = pd.read_csv('./sample.csv')

# centering
df_c = df - df.mean()
print(df_c.head(3))
print(df_c.describe())

# after centering
x = df_c['x']
y = df_c['y']

plt.scatter(x, y)
plt.show()
