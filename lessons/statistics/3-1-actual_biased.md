### [Think Stats Chapter 3 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2004.html#toc31) (Actual vs. Biased)

**Metis:**
This problem presents a robust example of actual vs biased data. As a data scientist, it will be important to examine not only the data that is available, but also the data that may be missing but highly relevant. You will see how the absence of this relevant data will bias a dataset, its distribution, and ultimately, its statistical interpretation.

**Exercise:**
Something like the class size paradox appears if you survey children and ask how many children are in their family. Families with many children are more likely to appear in your sample, and families with no children have no chance to be in the sample.

Use the NSFG respondent variable `numkdhh` to construct the actual distribution for the number of children under 18 in the respondents' households.

Now compute the biased distribution we would see if we surveyed the children and asked them how many children under 18 (including themselves) are in their household.

Plot the actual and biased distributions, and compute their means.

**Answer:**
The first order of business is to take a look at what the variable ```numkdhh``` represents. This is found in the ```2002FemResp.dct``` file. The listed description is """NUMBER OF BIO/ADOPT/RELATED/LEGAL CHILDREN UNDER AGE 18 IN HOUSEHOLD". Although this is not important for the scope of this question, it's important to understand what the variables represent before diving into the analysis.

To obtain a biased pmf distribution, the probability of each value occuring is multiplied by the value itself in order to give it more 'weight'. Each weighted probability is then divided by the sum of the weighted probabilities in order to normalize the distribution back to 1. In this case, you would be completely unable to capture households with 0 children based on the survey method.

Create dataframe object,a series from the numkdhh column, and create a PMF using the provided .Pmf method( ).
```
resp = nsfg.ReadFemResp()
num_kids = resp.numkdhh
num_kids_pmf = thinkstats2.Pmf(num_kids, label = 'unbiased')
```

Although I could have used the ```BiasPmf (pmf, label)``` function provided, I wanted to get a more hands-on understanding of what was going on in the background and decided not to use it and instead wrote my own code that didn't make use of the .Mult( ) and .Normalize( ) methods.


```
biased_tot_prob = 0
biased_dict = {}
for kids, prob in num_kids_pmf.Items():
    biased_tot_prob += prob * kids

for kids, prob in num_kids_pmf.Items():
    biased_dict[kids] = (prob*kids)/ biased_tot_prob
biased_pmf = thinkstats2.Pmf(biased_dict, label = 'biased')
```



```
for kids, prob in num_kids_pmf.Items():
    print('Number of children: {}, {}%'.format(kids,round(prob*100,2)))

Actual PMF
Number of children: 0, 46.62%
Number of children: 1, 21.41%
Number of children: 2, 19.63%
Number of children: 3, 8.71%
Number of children: 4, 2.56%
Number of children: 5, 1.07%
```
```
for kids, prob in biased_pmf.Items():
    print('Number of children: {}, {}%'.format(kids,round(prob*100,2)))

Biased PMF
Number of children: 0, 0.0%
Number of children: 1, 20.9%
Number of children: 2, 38.32%
Number of children: 3, 25.52%
Number of children: 4, 10.02%
Number of children: 5, 5.24%
```
As we can see above from the listed values for both pmf distributions, the biased probabilities have been weighted by a factor of their values.

The PMF plotted as steps also shows this.

```
thinkplot.PrePlot(2)
thinkplot.Pmfs([num_kids_pmf, biased_pmf])
thinkplot.Config(xlabel='Number of Children in Household', ylabel='PMF')
```
![PMF Plots](/home/jc98924/Metis/dsp/lessons/statistics/pmfplot.png)

```
print('Unbiased mean:',round(num_kids_pmf.Mean(),3))
print('Biased mean:',round(biased_pmf.Mean(),3))

Unbiased mean: 1.024
Biased mean: 2.404
```
