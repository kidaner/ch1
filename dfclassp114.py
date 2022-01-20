# core of pandas is DataFrame, class designed to efficiently handle data in tabular form
# provides column labeling as well as indexing for the rows/records similar to relational database

import pandas as pd
import numpy as np

df = pd.DataFrame([10, 20, 30, 40],
                  columns=['numbers'],
                  index=['a', 'b', 'c', 'd'])

df['floats'] = [1.5, 2.5, 3.5, 4.5]
df['names'] = ['Sandra', 'Lilli', 'Henry', 'Yves']

#
np.random.seed(100)
a = np.random.standard_normal((9, 4))

# pandas will retain basic structure of ndarray object and will only add metainfo index values
# represents typical use case for financial applications and scientific research

df = pd.DataFrame(a)
df.columns = ['No1', 'No2', 'No3', 'No4']

dates = pd.date_range('2019-1-1', periods=9, freq='M')

df.index = dates
print(df)
