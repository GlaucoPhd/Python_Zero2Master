# Graph Value of the Players Wage
# Use Seaborn instead of matplotlib
# Matplotlib is very extensive
# Seaborn is very easy and fast (Library Built on the top of Matplotlib)
# Bokeh interactive visualization
import pandas as pd
import seaborn as sns
data_frame = pd.read_csv('data.csv')
sns.set()
data_frame.shape

df1 = pd.DataFrame(data_frame, columns=['Name', 'Wage', 'Value'])


def value_to_float(x):
    if type(x) == float or type(x) == int:
        return x
    if 'K' in x:
        if len(x) > 1:
            return float(x.replace('K', '')) * 1000
        return 1000.0
    if 'M' in x:
        if len(x) > 1:
            return float(x.replace('M', '')) * 1000000
        return 1000000.0
    if 'B' in x:
        return float(x.replace('B', '')) * 1000000000
    return 0.0


wage = df1['Wage'].replace('[\€]', '', regex=True).apply(value_to_float)
value = df1['Value'].replace('[\€]', '', regex=True).apply(value_to_float)

df1['Wage'] = wage
df1['Value'] = value

df1['difference'] = df1['Value'] - df1['Wage']
df1.sort_values('difference', ascending=False)
print(df1)



# data_frame = pd.read_csv('data.csv')
# df1 = pd.DataFrame(data_frame, columns=['Name', 'Wage', 'Value'])
graph = sns.scatterplot(x='Wage', y='Value', data=df1)
graph()
