import pandas as pd
df = pd.DataFrame(['a', 'b', 'c', 'a'], columns=['Уникальное значение'])
one_hot_df = pd.DataFrame()
for unique_value in df['Уникальное значение'].unique():
    one_hot_df[unique_value] = (df['Уникальное значение'] == unique_value).astype(int)
print(one_hot_df)