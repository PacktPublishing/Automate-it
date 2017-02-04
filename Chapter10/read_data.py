import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

plt.style.use('default')
pd.set_option('display.line_width', 5000)
pd.set_option('display.max_columns', 60)

#Read funding data and get the first 5 rows
df = pd.read_csv('TechCrunchcontinentalUSA.csv')
print "First five rows:\n", df[:5]

df = pd.read_csv('TechCrunchcontinentalUSA.csv', index_col='fundedDate', \
                  parse_dates=['fundedDate'], dayfirst=True,)
print "Top five rows:\n", df[:5]

#Read a given column, in this case raisedAmt
raised = df['raisedAmt'][:5]
print "Funding Raised by Companies over time:\n", raised

#Visualize data on a plot
sns.set_style("darkgrid")
sns_plot = df['raisedAmt'].plot()
plt.ylabel("Amount Raised in USD"); plt.xlabel("Funding Year")
plt.savefig('amountRaisedOverTime.pdf')
