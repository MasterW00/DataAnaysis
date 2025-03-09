# Overview

I wanted to understand the power of Computational data analysis. In this project I try to combine two of my passions, cars and computers. I wanted to find interesting infromation that i can derive from the data found from cars.com on what they have sold on their store
{Provide a description of the data set that you are analyzing.  Include the link of where you obtained the data.}
I used a set of data containing information on cars sold at Cars.com
[Data Set](https://www.kaggle.com/datasets/georgejnr/used-and-new-cars-datasets) 

I wanted to initally answer different questions but i started with the mean prices of cars form each year. Then i wanted to filter out outliers to i looked for statistical methods for filtering extrenuous data. In this program i use the standard deviation of the prices in each year and filter out years whos standard deviations exceed that of the rest of the years in about the top 5%. The filtered chart showed one year had a significantly higher value than the others. This year is the year of the 1959 Porche 356. The unfiltered data showed that the Acura NSX T from 1996-2001 are very high value as well as some other hot models of cars. Then I was interested in the effects of the energy crisises back in the day compared to the standard means as well as the modern fuel crisis. For that i did a two sample test with the means of all the years compared to the means of crisises that occured in 1970 and 1980 then did the same with the crisis in the 2019-present as well as the different crisis periods compared to eachother.
{Provide a link to your YouTube demonstration.  It should be a 4-5 minute demo of the data set, the questions and answers, the code running and a walkthrough of the code.}

[Software Demo Video](https://youtu.be/t4VisNTMnCc)

# Data Analysis Results

What Year has the highest value based on the average value of the cars sold from that year?

The year 1959 takes the top position selling three porche 356 two of which were the A model.
1997 was the runner up selling several hot label cars such as Porches, Acura NSXs, and Corvetts

Do the fuel crisises in the classic periods have an effect on the cars values from those years?

These numbers as i have seen them are not close to 0.05. through this test
we can not make a conclusion however they are still very low.
They have shown there are some differneces in the mean prices of cars
because of the fuel crisis and could require ferther testing to understand.
They are not similar distributions however and the factor of fuel crisis might not be the reason for their
differneces to the sampled population.
having a larger population size as well as samples would yeild more accurate results.
Formulating other forms of tests would yeild more accurate results as well.

# Development Environment

Coded in Vscode basic python extensions 
Co-Pilot: directed me on methods I can use that i would search on the Pandas website to learn more about

Python - easy to use
NumPy, Pandas - DataAnalysis envirnment for data frames and other data manipulation and description methods
MathPlotLib - Data plotting and data discription visual elements
SciPy - Data description and analysis methods for scientific statistical analysis
# Useful Websites

* [SciPy Ttest for Significance](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.ttest_ind.html)
* [Pandas](https://pandas.pydata.org/docs/user_guide/basics.html)
* [Engineering Statistics Recource](https://en.wikipedia.org/wiki/Engineering_statistics)

# Future Work

* Which manufacturer makes the highest value cars
* Which car model is most prone to price fluctuation
* Do old cars raise or lower in value and is there a way to predict that
