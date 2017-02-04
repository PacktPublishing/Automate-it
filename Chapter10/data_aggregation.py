import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

#Set the plot style
plt.style.use('default')

#Set height and width of the plot
pd.set_option('display.line_width', 5000)
pd.set_option('display.max_columns', 60)

#Read the funding data with indexed column
df = pd.read_csv('TechCrunchcontinentalUSA.csv', index_col='fundedDate', \
                 parse_dates=['fundedDate'], dayfirst=True,)

funds = df[['raisedAmt', 'round']]
funds['month'] = funds.index.month
print "Funding Rounds with Month Index:\n", funds

#Funding rounds grouped by month
#Aggregate the amount raised
funding_by_month = funds.groupby('month').aggregate('sum')
funding_by_month.index = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'June', 'July', \
                              'Aug', 'Sept', 'Oct', 'Nov', 'Dec']
print "Funding Rounds Grouped By Month:\n", funding_by_month

#Plot funding rounds based on months
sns.set_style("darkgrid")
sns_plot = funding_by_month.plot(color='green')
plt.savefig('fundingGroupByMonth.pdf')

#Find funding rounds based on month and the round of funding
funds['month'] = funds.index.month
funding_by_stage = funds.groupby(['month', 'round']).aggregate('sum')
print funding_by_stage


