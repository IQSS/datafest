import pystan
from numpy import genfromtxt
golf_data = genfromtxt('golf_data.csv', delimiter=',', skip_header=1)
dat = {'obs' : len(golf_data), 'feet' : golf_data[:,0], 
'tries' : golf_data[:,1].astype(int), 'made' : golf_data[:,2].astype(int), 
'mu' : 1.0 / 15.0}
model1 = pystan.StanModel(file='golf1.stan', extra_compile_args=['-Os', '-g0'])  
post1 = model1.sampling(data=dat, refresh=0)
print(pystan.misc._print_stanfit(post1, pars=['beta']))
mat = post1.extract(permuted=True)
