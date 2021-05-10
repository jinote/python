## **Using Dask DataFrames**
**from datacamp**

### **Reading CSV**

```python
import dask.dataframe as dd

```

- dd.read_csv()
    - Accepts  single filename or glob pattern (with wildcard *)
    - Does not read file immediately (lazy evaluation)
    - File(s) need not fit in memory

### Reading multiple CSV files

%ls

quarter1.csv 

quarter2.csv

quarter3.csv

quarter4.csv

```python
transactions = dd.read_csv('*.csv')

transactions.head() # parts from the beginning
transactions.tail() # parts from the end
```

### Building delayed pipelines

```python
is_wendy = (transactions['names'] == 'Wendy')
wendy_amounts = transactions.loc[is_wendy, 'amount']
wendy_amounts

wendy_diff = wendy_amounts.sum()
wendy_diff

# visualization left to right with circle/
wendy_diff.visualize(rankdir = 'LR')
```

### Compatibility with Pandas API

Unavailable in dask.datarame

- some unsupported file formats (.xls, .zip, .gz)
- sorting

Available in dask.dataframe

- indexing, selection & reindexing
- aggregations: .sum(), .mean(), .std(), .min(), .max() etc
- .groupby()
- dd.to_datetime()

### Building a pipeline of delayed tasks

```python
# Read from 'WDI.csv': df
df = dd.read_csv('WDI.csv')

# Boolean series where 'Indicator Code' is 'EN.ATM.PM25.MC.ZS': toxins
toxins = df['Indicator Code'] == 'EN.ATM.PM25.MC.ZS'
# Boolean series where 'Region' is 'East Asia & Pacific':region
region = df['Region'] == 'East Asia & Pacific'

# Filter the DataFrame using toxins & region: filtered
filtered = df[toxins & region > 0]
```

### Grouping & Aggregating by year

```python
# plot the avg percent of the population exposed to air pollution in the East Asia & Pacific region from 2010 to 2015

yearly = filtered.groupby('Year')
yearly_mean = yearly.mean()
result = yearly_mean.compute()

# plot the 'value' column with .plot.line()
result['value'].plot.line()
plt.ylabel('% pop exposed')
pot.show()
```

### Timing Dask DataFrame Operations

How big is big data?

Two key questions:

- Data fits in RAM(random access memory)?
- Data fits on hard disk?

```python
%ll -h yellow_tripdata_2015-*.csv
```

### Timing I/O & Computation: Pandas

```python
import time, pandas as pd
t_strat = time.time();
df = pd.read_csv('yellow_tripdata_2015-01.csv');
t_end = time.time();
print('pd.read_csv(): {} s'.format(t_end-t_start)) #time [s]

t_start = time.time();
m = df['trip_distance'].mean();
t_end = time.time();
print('.mean(): {} ms'.format((t_end-t_start)*1000)) #time[ms]
```

### Timing I/O & Computation: Dask

- time saving

```python
import dask.dataframe as dd, time
t_start = time.time();
df = dd.read_csv('yellow_tripdata_2015-*.csv');
t_end = time.time();
print('dd.read_csv: {} ms'.format((t_end-t_start)*1000)) #time[ms = million seconds]

t_start = time.time();
m = df['trip_distance'].mean()
t_end = time.time();
print('.mean(): {} ms'.format((t_end - t_start)*1000)) #time[ms]

t_start = time.time();
result = m.compute();
t_end = time.time()l
print('.compute(): {} min'.format((t_end - t_start)/60)) #time[min]
```

### Timing in the IPython shell

```python
m = df['trip_distance'].mean()
%time result = m.compute()
```

### Is Dask or Pandas appropriate?

- How big is dataset?
- How much Ram available?
- How many threads/cores/CPUs available?
- Are Pandas computations/formats supported in Dask API?
- Is computataion I/O-bound (disk-intensive) or CPU-bound (processor intensive)?

Best use case for Dask

- Computations from Pandas API available in Dask
- Problem size close to limits of RAM, fits on disk

### Preparing the pipeline

```python
def by_region(df):
	# create the toxins array
	toxins = df['Indicator Code'] == 'EN.ATM.PM25.MC.ZS'
	
	# create the y2015 array
	y2015 = df['Year'] == 2015
	
	# Filter the df and group by 'Region'
	regions = df[toxins & y2015 > 0].groupby('Region')

	return regions['value'].mean()
```

### Comparing Dask & pandas execution times

```python
#pandas
df = pd.read_csv('WDI.csv')
t0 = time.time()
result = by_region(df)
t1 = time.time()
print((t1-t0)*1000)

#dask
t0 = time.time()
df = dd.read_csv("WDI.csv")
result = by_region(df)
t1 = time.time()
print((t1-t0)*1000)
```

### Analyzing NYC Taxi Rides

```python
# Read all .csv files: df
df = dd.read_csv('taxi/*.csv', assume_missing=True)

# Make column 'tip_fraction'
df['tip_fraction'] = df['tip_amount'] / (df['total_amount'] - df['tip_amount'])

# Convert 'tpep_dropoff_datetime' column to datetime objects
df['tpep_dropoff_datetime'] = dd.to_datetime(df['tpep_dropoff_datetime'])

# Construct column 'hour'
df['hour'] = df['tpep_dropoff_datetime'].dt.hour

# Filter rows where payment_type == 1: credit
credit = df[df['payment_type'] == 1]

# Group by 'hour' column: hourly
hourly = credit.groupby('hour')

# Aggregate mean 'tip_fraction' and print its data type
result = hourly['tip_fraction'].mean()
print(type(result))

# Perform the computation
tip_frac = result.compute()

# Print the type of tip_frac
print(type(tip_frac))

# Generate a line plot using .plot.line()
tip_frac.plot.line()
plt.ylabel('Tip fraction')
plt.show()
```
