import pandas as pd

df1 = pd.DataFrame(
                   columns=['letter', 'number'])
df2 = pd.DataFrame([['c', 3], ['d', 4]],
                   columns=['letter', 'number'])

df = pd.concat([df1, df2], ignore_index=True)

print(df)