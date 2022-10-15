import pandas as pd
import numpy as np

wadiz_list = [['1,','2','3','4'], ['5','6','7','8']]

df1 = pd.DataFrame(data=wadiz_list)
df1.to_csv("wadiz_test.csv",mode='w',encoding='utf-8-sig')