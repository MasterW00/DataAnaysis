import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy as sci
plt.close("all")

data = pd.read_csv('./data/car_data.csv') # Load the data
#data = data[:10000] #limited data computations while i was experimenting it would take forever for certain operations to compute but now its smooth and i can handel more then a hundred thoudand datapoints
def parse_price(price):
    #this function parses the prices of the cars
    try:
        num = float(price.replace('$', '').replace(',', '')) 
    except ValueError:
        return 0.0
    return num

grouped_data = data.groupby(['Year']) #we create a groupobject by smiliar indexes of year
grouped_data = grouped_data['Price'].agg(list).reset_index() #we aggregate the data by the prices in each year and make a list of cost of cars from those years 
grouped_data['Price'] = grouped_data['Price'].apply(lambda x: [parse_price(price) for price in x]) #parse each price to numbers we can use
grouped_data['StdDev'] = grouped_data['Price'].apply(np.std) #calculate the standard deviation of the prices for each year
grouped_data['MeanPrice'] = grouped_data['Price'].apply(np.mean) # calculate the mean of the prices for each year
normaldata = grouped_data[grouped_data['StdDev'] < 100000] #this is a specifically tuned outlier filter if the standard of deviation exceeds the natural deviation for the sample
allmeans = grouped_data['MeanPrice'] #a series of all the mean prices
means_from_fuel_crisis = grouped_data[(grouped_data['Year'] > 1972) & (grouped_data['Year'] < 1976) & (grouped_data['Year'] < 1980) &(grouped_data['Year'] < 1986)]['MeanPrice'] #this creates a specific series containg the mean prices of the cars made during fuel crisis
means_modern = grouped_data[(grouped_data['Year'] > 2018) & (grouped_data['Year'] < 2025)]['MeanPrice'] #this creats a series of modern cars from the most recent fuel crisis
ptest_fuel_crisis = sci.stats.ttest_ind(allmeans, means_from_fuel_crisis)
ptest_modern = sci.stats.ttest_ind(allmeans, means_modern)
ptest_crisis_compared = sci.stats.ttest_ind(means_from_fuel_crisis, means_modern)


#print(normaldata.head())
#print(grouped_data.head())
grouped_data.plot.bar(x ='Year', y='StdDev',legend=False) #this plots the standard deviation of the prices of cars from each year
plt.xlabel('Year')
plt.ylabel('Standard Deviation')
plt.title('Standard Deviation of Car Prices by Year')
plt.show()
grouped_data.plot.bar(x ='Year', y='MeanPrice',legend=False) #this plots the mean price of cars from each year over all
plt.xlabel('Year')
plt.ylabel('Mean Price')
plt.title('Mean Car Prices by Year - Unfiltered')
plt.show()
normaldata.plot.bar(x ='Year', y='MeanPrice',legend=False) #this plots the mean price of cars from each year after filtering
plt.xlabel('Year')
plt.ylabel('Mean Price')
plt.title('Mean Car Prices by Year - Filtered')
plt.show()

print('Which car causes this spike in 1959?')
print(data[data['Year'] == 1959]) #found a porshe 356, classic!
print()
#test if we can reject the null hypothesis that population mean = crisis mean at 0.05 significance
print('The closer these values get to 0.05, the more likely these events were disruptive to the mean car price of that period')
print('Classic car prices today due to the old fuel crisises')
print(1 - ptest_fuel_crisis.pvalue)
print()
print('Modern car prices today due to the new fuel crisises')
print(1 - ptest_modern.pvalue)
print()
#test if we fail to reject the null hypothesis that modern fuel crisis mean = classic fuel crisis mean at 0.05 significance
print('The closer this number to 0.05 the more alike both fuel crisis periods were')
print(ptest_crisis_compared.pvalue)
"""
===================================================================================
output:
Classic car prices today due to the old fuel crisises
0.19509524131049938

Modern car prices today due to the new fuel crisises
0.11588325576447223

The closer this number to 0.05 the more alike both fuel crisis periods were
0.40835229645089866
===================================================================================
Conclusion:
-------------
These numbers as i have seen them are not close to 0.05. through this test
we can not make a conclusion however they are still very low.
They have shown there are some differneces in the mean prices of cars
because of the fuel crisis and could require ferther testing to understand.
They are not similar distributions however and the factor of fuel crisis might not be the reason for their
differneces to the sampled population.
having a larger population size as well as samples would yeild more accurate results.
Formulating other forms of tests would yeild more accurate results as well.
====================================================================================
"""

#print(1 - sci.stats.ttest_ind(allmeans, allmeans).pvalue) shows the there is no difference in these standard deviations and we can not reject the null hypothesis however the 1 - (...) shows us that at 0.05 we can not reject versus if we can reject

#print(data[data['Year'] == 1997]) #found the Acura NSX, nice car ;)

#print(data[data['Year'] == 1991]) #found some more NSX's and some porches, beetles, and corvettes 
#print(data[data['Year'] == 1992]) 
#print(data[data['Year'] == 2001]) 


