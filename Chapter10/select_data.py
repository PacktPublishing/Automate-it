import pandas as pd
#Make the graphs a bit prettier, and bigger
from matplotlib import pyplot as plt
plt.style.use('default')

pd.set_option('display.line_width', 5000)
pd.set_option('display.max_columns', 60)

fundings = pd.read_csv('TechcrunchcontinentalUSA.csv')
print "Type of funding:\n", fundings[:5]['round']

#Selecting multiple columns
print "Selected company, category and date of funding:\n",\
    fundings[['company', 'category', 'fundedDate']][600:650]

#Most common category of company that got funded
counts = fundings['category'].value_counts()
print "Count of common categoris of company that raised funds:\n", \
    counts

#Plot the data in horizontal bar chart
counts.plot(kind='barh', )
plt.xlabel("Count of categories")
plt.savefig('categoriesFunded.pdf')
