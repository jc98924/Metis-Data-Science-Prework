[Think Stats Chapter 2 Exercise 4](http://greenteapress.com/thinkstats2/html/thinkstats2003.html#toc24) (Cohen's d)

**Exercise 2.4 Using the variable totalwgt_lb, investigate whether first babies are lighter or heavier than others. Compute Cohen’s d to quantify the difference between the groups. How does it compare to the difference in pregnancy length?**

>> The Cohen's d value computed for the size effect between first born children and all other children is -0.0887. This signifies that the difference in average weight is .0887 standard deviations, with first born children being relatively lighter. Based on Cohen's suggestions (listed below), the calculated value signifies a 'small' effect size for the given the dataset. Compared to the Cohen's d value for pregnancy length which is 0.0289, it does hold a slightly larger effect but both measures are considered small.

Effect size	| d	|Reference
------------|---|-----------
Very small|	0.01| Sawilowsky, 2009
Small |	0.20| Cohen, 1988
Medium | 0.50 |	Cohen, 1988
Large| 0.80 | Cohen, 1988
Very large | 1.20 |	Sawilowsky, 2009
Huge | 2.0 | Sawilowsky, 2009



**Code:**
```
import math
import pandas as pd
import numpy as np
import nsfg
import thinkstats2003

preg = nsfg.ReadFemPreg()
live_births = preg[preg.outcome == 1]

first_born = live_births[live_births.birthord == 1]
other_born = live_births[live_births.birthord != 1]

first_wgt = first_born.totalwgt_lb
other_wgt = other_born.totalwgt_lb

def CohenEffectd(firstborn, otherborn):
    mean_diff = firstborn.mean() - otherborn.mean()
    var_first, var_other = firstborn.var(), otherborn.var()
    n1, n2 = len(firstborn), len(otherborn)
    pooled_variance = (n1 * var_first + n2 * var_other)/ (n1 + n2)
    d = mean_diff / math.sqrt(pooled_variance)
    return d

CohenEffectd(first_wgt, other_wgt)

>> -0.088672927072602



```
