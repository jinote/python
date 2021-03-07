# 9660_Regression self-study & practice

import pandas as pd
tayko_df = pd.read_csv('/Users/hojin/Desktop/9660_datasets/Tayko.csv')

# rename a column
tayko_df.rename(columns = {'Web order':'Web_order'}, inplace = True)

# extract columns that I want
tayko_df.loc[:,['Freq','last_update_days_ago', 'Web_order','Gender=male','Address_is_res','US','Spending']]

# use pivot table
import numpy as np
tayko_df.pivot_table(values = 'Spending', index = 'Gender=male', aggfun = [np.mean, np.std]) 
