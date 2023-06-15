import csv
import numpy as np
import pandas as pd
import requests

# mostrar o arquivo 

df = pd.read_csv('/home/senai/Downloads/K3241.K03200Y1.D30513.ESTABELE', 
                encoding= 'latin1', sep=';',
                dtype='string', chunksize= 10000)
df
print(df)

for mini_df in df:
    print(mini_df)
    break