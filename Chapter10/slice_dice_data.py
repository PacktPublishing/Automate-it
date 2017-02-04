import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

plt.style.use('default')

pd.set_option('display.line_width', 5000)
pd.set_option('display.max_columns', 60)

funding = pd.read_csv('TechcrunchcontinentalUSA.csv', index_col='fundedDate', \
                  parse_dates=['fundedDate'], dayfirst=True)

#Get Web fundings in CA
web_funding = funding['category'] == 'web'
in_CA = funding['state'] == 'CA'
in_city = funding['city'].isin(['Palo Alto', 'San Francisco',
                                 'San Mateo', 'Los Angeles', 'Redwood City'])
print "Filtered Data:\n", funding[web_funding & in_CA & in_city]

#Get Funding rounds for companies in 'web' category by cities in CA
web_funding = funding[web_funding & in_CA & in_city]
web_counts = web_funding['city'].value_counts()
print "Funding rounds for companies in 'web' category by cities in CA:\n", web_counts

#Funding rounds for companies in all categories in CA
total_funding = funding[in_CA & in_city]
total_counts = total_funding['city'].value_counts()
print "Funding rounds for companies in 'all' categories by cities in CA:\n",total_counts

#Plot the horizontal bar chart to generate insights
sns.set_style("darkgrid")
sns_plot = (web_counts*100/total_counts.astype(float)).plot(kind='barh')
plt.xlabel("(Funding Rounds in Web Category) / (Funding Rounds in All Categories) * (100)")
plt.savefig('webFundedByCity.pdf')
