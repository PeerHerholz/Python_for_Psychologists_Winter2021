# The script was written using Python 3.7

print("Downloading data")
import requests
url = 'https://openneuro.org/crn/datasets/ds003709/snapshots/1.0.0/files/participants.tsv'
r = requests.get(url, allow_redirects=True)
open('participants.tsv', 'wb').write(r.content)

print("Checking data")
import pandas as pd
data = pd.read_csv('participants.tsv', sep='\t', na_values=".")
print(data.describe())

groupby_group = data.groupby('group')
for group, value in groupby_group['MFQ']:
     print((group, value.mean()))

print(groupby_group.mean())

print("Plotting data based on groups")
import matplotlib.pyplot as plt
groupby_group.boxplot(column=['age', 'MFQ', 'SHAPS']);
plt.savefig('data_grouped_box.png')

print("Plotting one variable interactively")
import plotly.express as px
from plotly.offline import plot

fig = px.histogram(data['MFQ'], marginal='box', template='plotly_white')

fig.update_layout(showlegend=False, width=800, height=600)

#fig.show()

plot(fig, filename = 'labels.html')

print("creating raincloud plots for one variable")
import ptitprince as pt

pal = "Set2"

dx = "group"; dy = "SHAPS"
f, ax = plt.subplots(figsize=(12, 5))
ax=pt.RainCloud(x = dx, y = dy,  data = data, palette = pal, bw = .2, width_viol = .7,
                ax = ax, orient ='h' , alpha = .65, dodge = True,  move = .2)
plt.show()
f.savefig('data_raincloud.png')

print("creating a pairplot for variables")
import seaborn as sns
sns.pairplot(data, hue='group')
plt.show()

sns.pairplot(data, hue='group')
plt.savefig('data_pairplot.png')

print("compute correlation between variables")
import pingouin as pg
pearson_correlation = pg.corr(data['MFQ'], data['SHAPS'])
print(pearson_correlation)

print("checking normality of one variable")
print(pg.normality(data['MFQ']))

print("computing paired t-test between groups")
MDD_MFQ = data[data['group'] == 'MDD']['MFQ']
HV_MFQ = data[data['group'] == 'HV']['MFQ']
print(pg.ttest(MDD_MFQ, HV_MFQ))

print("computing non-parametric test between groups")
print(pg.mwu(MDD_MFQ, HV_MFQ))

print("computing GLM for one variable")
from statsmodels.formula.api import ols
model = ols("MFQ ~ group + 1", data).fit()
print(model.summary())
