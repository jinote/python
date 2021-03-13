# Introduciton to relational plots and subplots
# Quesion about quantitiative variables
'''Height vs weight, 
Number of school absences vs final grade,
GDP vs percent literate'''

# relplot()
## create 'relational plots': scatter or line
## why relplot(), not scatterplot()?
## relplot() lets you create subplots in a single figure

# Using scatterplot()
import seaborn as sns
import matplotlib.pyplot as plt
sns.scatterplot(x='total_bill',
                y='tip',
                data=tips)

plt.show()

# Using replot()
import seaborn as sns
import matplotlib.pyplot as plt

sns.relplot(x='total_bill',
            y='tip',
            data=tips
            kind='scatter')

plt.show()

import seaborn as sns
import matplotlib.pyplot as plt

# subplots in columns (horizontally arranged)
sns.relplot(x='total_bill',
            y='tip',
            data=tips,
            kind='scatter',='
            col='smoker')

plt.show()

# subplots in rows (vertically arranged)
sns.relplot(x='total_bill',
            y='tip',
            data=tips,
            kind='scatter',
            row = 'smoker')

plt.show()

# subplots in rows and columns
import seaborn as sns
import matplotlib.pyplot as plt
sns.relplot(x='total_bill',
            y='tip',
            data=tips,
            kind='scatter',
            row='time')

plt.show()

# wrapping columns
sns.relplot(x='total_bill',
            y='tip',
            data=tips,
            kind='scatter',
            col='day',
            col_wrap=2)

plt.show()
            
# ording columns
sns.relplot(x='total_bill',
            y='tip',
            data=tips,
            kind='scatter',
            col='day',
            col_wrap=2,
            col_order=['Thur', 'Fri', 'Sat', 'Sun'])
            
plt.show()

# Customizing scatter plots
# subgroups with point size
import seaborn as sns
import matplotlib.pyplot as plt
sns.relplot(x='total_bill',
            y='tip',
            data=tips,
            kind='scatter',
            size='size',
            hue='size')
plt.show()

# subgroups with point style
import seaborn as sns
import matplotlib.pyplot as plt
sns.relplot(x='total_bill',
            y='tip',
            data=tips,
            kind='scatter',
            hue='smoker',
            style='smoker')

plt.show()

# changing point transparency
import seaborn as sns
import matplotlib.pyplot as plt

# set alpha(transparency) to be between 0 and 1
sns.relplot(x='total_bill',
            y='tip',
            data=tips,
            kind='scatter',
            alpha=0.4)
plt.show()
