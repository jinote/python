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

'''PCA: Principle Components Analysis
goal: redece a set of numerical variables.
create new variables that are linear combinations of the original variables
(ex, they are weighted averages of the original variables)'''

pcs = PCA(n_components=3)
pcs.fit(cereals_df[['calories', 'rating', 'sugars', 'fat', 'carbo']])
pcsSummary = pd.DataFrame({'Standard deviation': np.sqrt(pcs.explained_variance_),
                           'Proportion of variance': pcs.explained_variance_ratio_,
                           'Cumulative proportion': np.cumsum(pcs.explained_variance_ratio_)})

pcsSummary = pcsSummary.transpose()
pcsSummary.columns = ['PC1', 'PC2', 'PC3']
pcsSummary.round(4)

'''                     PC1	  PC2	   PC3	   PC4	   PC5
Standard deviation	22.8391	9.1902	4.0846	1.7160	0.4184
Proportion of variance	0.8334	0.1349	0.0267	0.0047	0.0003
Cumulative proportion	0.8334	0.9684	0.9950	0.9997	1.0000'''
