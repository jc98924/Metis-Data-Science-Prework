### [Think Stats Chapter 5 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2006.html#toc50) (blue men)

**Metis:**
This is a classic example of hypothesis testing using the normal distribution. The effect size used here is the Z-statistic.

**Excercise:**
Exercise 5.1 In the BRFSS (see Section 5.4), the distribution of heights is
roughly normal with parameters μ = 178 cm and σ = 7.7 cm for men, and
μ = 163 cm and σ = 7.3 cm for women.
In order to join Blue Man Group, you have to be male between 5’10” and
6’1” (see http://bluemancasting.com). What percentage of the U.S. male
population is in this range? Hint: use scipy.stats.norm.cdf.

**Answer:**

Given that height is roughly normally distributed and we know the values for mu (mean) and sigma (std), the value of the CDF can be calculated for the lower and upper bound of the acceptable heights. The difference between these two values will give us the percentage of the U.S. male population that falls within the range.


---

Import the stats module from ScipPy
```
from scipy import stats
```
μ and σ are given in cm, so it makes sense to convert the two heights into cm.

```
def conv_height(feet, inches):
    height = (feet*30.48) + (inches*2.54)
    return format(height,'.2f')

```
Using ```stats.norm``` along with the given mean and standard deviation, we are able to create a normal distribution for height. Using the .cdf method, we are then able to calculate the respective percentile ranks for the given percentile values of lower and upper height. The function is shown below.

```
def percentage_in_range(mu, sigma, lower_height, upper_height):
    """
    Function that creates a normal distribution given the mean and
    standard deviation and returns the percentage expected to fall
    within the lower and upper bound for height.
    ----
    args: mu, sigma, lower_height, upper_height
    return: percentage within range; (cdf(upper) - cdf(lower))*100
    """

    # Create the normal distribution given the mu and sigma
    norm_dist_height = stats.norm(loc = mu, scale = sigma)

    # Calculate the percentile rank given the values of height
    lower_cdf = norm_dist_height.cdf(lower_height)
    upper_cdf = norm_dist_height.cdf(upper_height)

    return "{} % of the U.S. male population is in this range.".format(round((upper_cdf - lower_cdf)* 100,2))
```

Using this function, we can set the inputs to determine our answer.
```
mu = 178
sigma = 7.7
lower_height = conv_height(5,10)
upper_height = conv_height(6,1)

percentage_in_range(mu, sigma, lower_height, upper_height)

>> '34.27 % of the U.S. male population is in this range.'

```
