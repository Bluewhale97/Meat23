#DBTITLE 1, Seaborn
# a lib that uses matplotlib underneath to plot grahs, it will be used to visualize random distribution

#1. distribution plot
#sns.displot([1,2,4,9,14,2])

#2. without histogram
#sns.distplot([1,2,4,9,14,2], hist=False)

#3. normal distribution, random.normal(loc, scale, size), loc is the x bar, scale is std, and size is the shape of array
# a=np.random.normal(2,10,(3,5))
# sns.distplot(a, hist=False)

#4. binomial distribution, describing the outcome of binary scenarios, random.binomial(n,p, size)
# a=np.random.binomial(10,0.2, (3,5))
# sns.distplot(a,hist=False, label='binomial')

#5. diff: binomial v.s. normal 
#binomial is discrete distribution whereas normal distribution is continuous

#6. poisson dist: discrete distribution, random.poison(lam, size), lam is the rate or know number of occurrence
# sns.distplot(np.random.poisson(lam=3,size=(100)), kde=False)
# plt.show()

#when poisson and binomial distributions are getting large enough, it will become similar to normal distribution, binomial dist has 2 outcomes but poisson has unlimited, but for very large n & very small p, n*p => lam, almost

#7. uniform distribution, used to describe every event has euqal change of occuring
# x=random.uniform(a,b,size), a is the lower bound, default 0, b is upper bound, default 1, size is the shape
# x=np.random.uniform(0,1,(3,5))
# sns.displot(x,hist=False)

#8.logistic distribution: used to describe growth, x=random.logistic(loc, scale, size)
# x=np.random.logistic(0,1,100)
# sns.distplot(x,hist=False)

#9. diff: logitsic v.s. normal 
#they are near identical, has more under tails. so for higher std, the normal & logistic distributions are near identical, apart from the peak

#10. multinomial dist, random.multinomial(n=6, pvals=,size=), n is number of times for each iteration, pvals is the possibility of each outcome, size is the size of iterations
# x=np.random.multinomial(n=20, pvals=[0.2,0.2,0.2,0.2,0.2], size=2)
# sns.distplot(x)

#11. exponential distribution, random.exponential(scale=,size=), scale is the exponent
# x=np.random.exponential(3,(2,3))
# sns.distplot(x)
# #diff between poisson and exponential distribution
# #poisson deals with numner of occ of an event in a time period whereas exponential distribution deals with the time between these event

#12. chi-square: used as a basis to verify the hypothesis
#random.chisquare(df,size)#df is the degree of freedom
# x=np.random.chisquare(3, 100)
# sns.distplot(x)

#13. rayleign distribution: used in signal processing
#x=random.rayleigh(scale=2,size=(2,3))
# x=np.random.rayleigh(scale=2,size=(2,3))
# sns.distplot(x)

#14. Pareto distribution: i.e. 80-20 distribution
x=np.random.pareto(a=2,size=3)
sns.distplot(x)

#15. zipf distribution: zipf's law is the nth common term is 1/n times of the most common term, for example, the 5th most common word in English is nearly 1/5 times as often as the most common word
x=random.zipf(a=2,size=3)
sns.distplot(x)
