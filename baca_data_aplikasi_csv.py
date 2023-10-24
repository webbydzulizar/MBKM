import re
import pandas as pd
import numpy as np

df_mag = pd.read_csv('D:/TEL-U/Semester 7/MBKM/Data_3habel_noobjek_m.csv')
df_res = pd.read_csv("D:/TEL-U/Semester 7/MBKM/Data_3habel_noobjek_r.csv")
#print(textfile)
filter_mag = df_mag ['FFt Magnitude']
filter_res = df_res ['Respiro']

# change any other character
df_mag ['Ubah'] = filter_mag.str.extract(pat = '([^\[]+(?=\]))')
print (df_mag ['Ubah'])
df_res ['Ubah2'] = filter_res.str.extract(pat = '([^\[]+(?=\]))')
print (df_res ['Ubah2'])
# new data frame with split value columns
new_mag = df_mag ['Ubah'].apply(lambda x: pd.Series(str(x).split(",")))
new_res = df_res ['Ubah2'].apply(lambda x2: pd.Series(str(x2).split(",")))

new_mag.to_csv("D:/TEL-U/Semester 7/MBKM/New_Data_3habel_noobjek_m.csv", encoding='utf-8', index = False, header=None)
new_res.to_csv("D:/TEL-U/Semester 7/MBKM/New_Data_3habel_noobjek_r.csv", encoding='utf-8', index = False, header=None)

        