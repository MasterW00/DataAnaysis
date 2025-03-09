# Overview

{Important!  Do not say in this section that this is college assignment.  Talk about what you are trying to accomplish as a software engineer to further your learning.}
I wanted to understand the power of Computational data analysis. In this project I try to combine two of my passions, cars and computers. I wanted to find interesting infromation that i can derive from the data found from cars.com on what they have sold on their store
{Provide a description of the data set that you are analyzing.  Include the link of where you obtained the data.}
I used a set of data containing information on cars sold at Cars.com
[Data Set](https://www.kaggle.com/datasets/georgejnr/used-and-new-cars-datasets) 
{Describe your purpose for writing this software to analyze the data.}
I wanted to initally answer different questions but i started with the mean prices of cars form each year. Then i wanted to filter out outliers to i looked for statistical methods for filtering extrenuous data. In this program i use the standard deviation of the prices in each year and filter out years whos standard deviations exceed that of the rest of the years in about the top 5%. The filtered chart showed one year had a significantly higher value than the others. This year is the year of the 1959 Porche 356. The unfiltered data showed that the Acura NSX T from 1996-2001 are very high value as well as some other hot models of cars. Then I was interested in the effects of the energy crisises back in the day compared to the standard means as well as the modern fuel crisis. For that i did a two sample test with the means of all the years compared to the means of crisises that occured in 1970 and 1980 then did the same with the crisis in the 2019-present as well as the different crisis periods compared to eachother.
{Provide a link to your YouTube demonstration.  It should be a 4-5 minute demo of the data set, the questions and answers, the code running and a walkthrough of the code.}

[Software Demo Video](http://youtube.link.goes.here)

# Data Analysis Results

{List the questions and the answers you found by doing this analysis.}

# Development Environment

{Describe the tools that you used to develop the software}
Coded in Vscode basic python extensions 
Co-Pilot: directed me on methods I can use that i would search on the Pandas website to learn more about
{Describe the programming language that you used and any libraries.}
Python - easy to use
NumPy, Pandas - DataAnalysis envirnment for data frames and other data manipulation and description methods
MathPlotLib - Data plotting and data discription visual elements
SciPy - Data description and analysis methods for scientific statistical analysis
# Useful Websites

{Make a list of websites that you found helpful in this project}
* [SciPy Ttest for Significance](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.ttest_ind.html)
* [Pandas](https://pandas.pydata.org/docs/user_guide/basics.html)
* [Engineering Statistics Recource](https://en.wikipedia.org/wiki/Engineering_statistics)

# Future Work

{Make a list of things that you need to fix, improve, and add in the future.}
* Which manufacturer makes the highest value cars
* Which car model is most prone to price fluctuation
* Do old cars raise or lower in value and is there a way to predict that