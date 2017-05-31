import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
##import plotly.plotly as py
##import plotly.graph_objs as go
##import plotly
##import cufflinks as cf
import seaborn as sns

df = pd.read_csv('EXSC-01-14RD CLIENT DATA TABLE.csv')

# zscores = sns.load_dataset("EXSC-01-14RD CLIENT DATA TABLE.csv")

zc = df[['EP-1','EP-2','EP-3','EP-4','EP-5','EP-6','EP-7','EP-8','EP-9']]
##trace = go.Heatmap(z=zc)
##data=[trace]
##py.iplot(data, filename='zscores')

##plotly.offline.plot({
##	"data": trace
##	})
##plotly.offline.plot({
##	"data": data
##	})
sns.heatmap(zc)
ax = sns.heatmap(zc)
plt.plot(ax)
