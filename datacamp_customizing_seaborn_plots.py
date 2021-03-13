# changing plot style and color
# figure "style" includes background and axes: seaborn has 5 styles
## preset options: "white", "whitegrid", "dark", "darkgrid", "ticks"
sns.set_style()

# default figure style ("white")
sns.catplot(x="age",
            y="masculinity_important",
            data=masculinity_data,
            hue="feel_masculine",
            kind="point")
plt.show()

# figure style: "whitegrid"
sns.set_style("whitegrid") # 그래프 배경에 격자생김
sns.set_style("ticks") # similar to white but x 및 y 축에 작은 눈금 추가
sns.set_style("dark") # gray background
sns.set_style("darkgrid") # gray + grid background


# changing the palette (set_style 컬러 바꾸기)
## figure "palette" changes the color of the main elements of the plot
sns.set_palette()
## use preset palettes or create a custom palette
# Diverging (나뉘는) palettes - 컬러가 진했다가 중간에 약해졌다가 다시 진해짐
# 1) "RdBu": red, light red........ light blue, blue
# 2) "PRGn": purple, light purple..........light green, green
# 3) "RdBu_r": r is short for reverse, meaning that "RdBu" reverse
# 4) "PRGn_r"

# Example (defulat palette)
category_order = ["No answer",
                  "Not at all",
                  "Not very",
                  "Somewhat",
                  "Very"]
sns.catplot(x = "how_masculine",
            data = masculinity_data,
            kind = "count",
            order = category_order)

plt.show()

# 위에서 palette 사용해 컬러 조정
sns.set_palette("RdBu") # 상단에 추가하면 됨


# sequential palettes - 컬러가 순차적으로 진해짐
# good example of sequential palettes: mpg vs horsepower 
# custom palettes
custom_palette = ['red', 'green', 'orange', 'blue', 'yellow', 'purple']
sns.set_palette(custom_palette)

custom_palette = ['#FBB4AE', '#B3CDE3', '#CCEBC5', '#DECBE4', '#FED9A6', '#FFFFCC', '#E5D8BD', '#FDDAEC', '#F2F2F2']
sns.set_palette(custom_palette)

# changing the scale
## figure "context" changes the scale of the plot elements and labels
sns.set_context() # x축, y축 폰트크기 작게 또는 크게 만들기
# smallest to largest: "paper", "notebook", "talk", "poster"
# default contest: "paper"
# 'talk' 으로 설정하려면 sns.set_context('talk')
sns.set_context('talk')
sns.catplot(x='age',
            y='masculinity_important',
            data=masculinity_data,
            hue='feel_masculine',
            kind='point')
plt.show()

# Adding titles and labels: Part1 
## creating informative visualizations
## Seaborn plots create two different types of objects: 
### 1) FacetGrid 
### 2) AxesSubplot objects

# 변수 type 알기 위해선 type(g)
g = sns.scatterplot(x="height", y="weight", data=df)
type(g) # matplotlib.axes._subplots.AxesSubplot

# 1) Adding a title to FacetGrid
g = sns.catplot(x="Region", y="Birthrate", data=gdp_data, kind="box")
g.fig.suptitle("New Title") # FacetGrid
plt.show()

# title 위치 조정하기: the default of y is 1
g = sns.catplot(x="Region",
                y="Birthrate",
                data=gdp_data,
                kind="box")
g.fig.suptitle("New Title", y = 1.03)
plt.show()

# 2) Adding a title to AxesSubplot
g = sns.boxplot(x="Region", 
                y="Birthrate",
                data=gdp_data)

g.set_title("New Title", y = 1.03) # AxesSubplot 

# Titles for subplots
g = sns.catplot(x="Region",
                y="Birthrate",
                data=gdp_data,
                kind="box",
                col="Group")

g.fig.suptitle("New Title",
               y=1.03)

g.set_titles("This is {col_name}")

# Adding axis labels: 
g = sns.catplot(x="Region",
                y="Birthrate",
                data=gdp_data,
                kind="box")
g.set(xlabel="New X Label",
      ylabel='New Y Label")

plt.show()
      
# Rotating x-axis tick labels
g = sns.catplot(x="Region",
                y="Birthrate",
                data=gdp_data,
                kind="box")
plt.xticks(rotation=90)
plt.show()

### Rotate x-tick labels
plt.xticks(rotation=90)
      
 
      
# 총정리
# Relational plots
# Show the relationship btw quantitative variables
# scatter plots, line plots
sns.relplot(x='x_variable_name',
            y='y_variable_name',
            data=pandas_df,
            kind='scatter')
      
# categorical plots
# show the distribution of a quantitative variable within categories defiend by a categorical variable
# : bar, count, box, point plots
sns.catplot(x='x_variable_name',
            y='y_variable_name',
            data=pandas_df,
            kind='bar')
# change the backgroud:
      sns.set_style()
# chagne the main element colors:
      sns.set_palette()
# change the scale:
      sns.set_context()
      
# Adding a title
FacetGrid = [relplot(), catplot()] = g.fig.suptitle()
AxeSubplot = [scatterplot(), countplot(), etc] = g.set_title()

# Final touches: Add x- and y-axis labels:
g.set(xlabel="new x-axis label",
      ylabel="new y-axis label")
      
# roate x-tick labels:
      plt.xticks(rotation=90)
      
      
