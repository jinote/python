# two types of relational plots:
## 1) scatter plots
## Each plot point is an  independent observation
## 2) line plots
## Each plot point represents the same 'thing', typically tracked over time

import matplotlib.pyplot as plt
import seaborn as sns
sns.relplot(x='hour',y='No_2_mean',
            data=air_df_mean,
            kind='line',
            style='location',
            hue='location')
plt.show()

#Adding markers
sns.relplot(x='hour',y='No_2_mean',
            data=air_df_loc_mean,
            style='location',
            hue='location',
            markers=True, # adding markers
            dashes=False) # using solid lines for all countries,while still allowing for different marker styles for each line.

plt.show()
            
  
# multiple observation per x-value
# shaded region is the confidence interval
## assumes dataset is a random sample
## 95% confident that the mean is within this interval
## indicates uncertainty in our estimate

# replacing confidence interval with standard deviation
import matplotlib.pylot as plt
import seaborn as sns

sns.relplot(x='hour',y='No_2',
            data=air_df,
            kind='line',
            ci='sd') # OR ci= None

plt.show()

