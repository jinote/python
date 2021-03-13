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
            ci='sd') # OR ci= None # getting rid of confidence interval

plt.show()

# categorical plots  1) count plots
# comparisons between groups

# catplot()
# Used to create categorical 

import matplotlib.pyplot as plt
import seaborn as sns
sns.catplot(x='how_masculine',data=masculiniity_data,
            kind='count')
plt.show()

# changing the order
import matplotlib.pylot as plt
import seaborn as sns
category_order=['No answer','Nat at all','Not very','Somewhat','Very']
sns.catplot(x='how_masculine',data=masculinity_data,
            kind='count', order=category_order)
plt.show()
         
# bar plots: displays mean of quantitative variable per category
import matplotlib.pyplot as plt
import seaborn as sns

sns.catplot(x='day',
            y='total_bill',
            data=tips,
            kind='bar')

plt.show()

# Confidence intervals
## lines show 95% confidence intervals for the mean
## shows uncertainty about our estimate
## assumes our data is a random sample

sns.catplot(x='day',
            y='total_bill',
            data=tips,
            kind='bar',
            ci=None) 
plt.show()


# box plot
## shows the distribution of quantitative data
## see median, spread, skewness, outliers
## facilitates comparisons between groups

import matplotlib.pyplot as plt
import seaborn as sns
g = sns.catplot(x="time",y="total_bill", data=tips,
            kind="box")
plt.show()


# change the order of categories
g =sns.catplot(x="time", y="total_bill", data=tips,
               kind="box", order = ["Dinner", "Lunch"])
plt.show()

# omitting the outliers using 'sym'
g=sns.catplot(x='time',y='total_bill',data=tips,kind='box,
              sym='')

plt.show()

# changing the whiskers using 'whis'
## by default, the whiskers extend to 1.5* the interquartile range
## Make them extend to 2.0 * IQR: whis=2.0
## show the 5th and 95th percentiles: whis=[5,95]
## show min and max values: whis=[0,100]

import matplotlib.pyplot as plt
import seaborn as sns
g= sns.catplot(x="time", y="total_bill",
               data=tips, kind="box",
               whis=[0,100])



# point plots
## points show mean of quantitative variable
## vertical lines show 95% confidence intervals

# point plots vs. line plots?
## both shows: 1) means of quantitative variable 
             # 2) 95% confidence intervals for the mean
## Differences: Line plot - quantitative variable (usually time) on x-axis
              # Point plot - categorical variable on x-axis
# creating a point plot
import matplotlib.pyplot as plt
import seaborn as sns
sns.catplot(x="age", y="masculinity_important",
            data=masculinity_data,
            hue = "feel_masculine",
            kind="point")

# disconnecting the points
import matplotlib.pyplot as plt
import seaborn as sns
sns.catplot(x="age", y="masculinity_important",
            data=masculinity_data,
            hue="feel_masculine",
            kind="point",
            join=False)
plt.show()

# displaying the median 
## we want to use median instead of mean because if there are a lot of outliners, median could be a better way.
import matplotlib.pyplot as plt
import seaborn as sns
from numpy import median
sns.catplot(x="smoker",y="total_bill",
            data=tips,
            kind="point",
            estimator=median)

plt.show()

# customozing the confidence intervals
# -로 신뢰구간 표시하기 
# capsize = 0.2
import matplotlib.pyplot as plt
import seaborn as sns
sns.catplot(x="smoker",
            y="total_bill",
            data=tips,
            kind="point",
            capsize=0.2)
plt.show()

# turning off confidence intervals
import matplotlib.pyplot as plt
import seaborn as sns

sns.catplot(x="smoker",
            y="total_bill",
            data=tips,
            kind="point",
            ci=None) # confidence interval 표시된 부분 제거하기 
plt.show()
