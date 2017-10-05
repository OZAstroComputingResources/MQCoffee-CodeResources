from scipy import stats
from scipy.signal import argrelextrema
from scipy.stats import norm
import ast
import math
import matplotlib.lines as mlines
import matplotlib.pyplot as plt
import numpy as np
import pickle
import random
import scipy
import sys


import emcee


###########################################
#                                         #
#        Generate a noisy Gaussian        #
#                                         #
###########################################

# parameters of Gaussian
real_mean = 0.0
real_fwhm = 1.5
real_height = -3.0
rms = 0.1

def AddNoise(y_values, x_axis, rms):
	'''
	Adds noise to a spectrum.
	'''
	noise_spectrum = np.random.randn(len(x_axis)) * rms

	synthetic_data = y_values + noise_spectrum
	return synthetic_data
def Gaussian(mean, fwhm, height):
	return lambda x: height * np.exp(-4.0 * np.log(2.0) * (x - mean)**2.0 / fwhm**2.0)

# generate synthetic data that we'll then fit
x_axis = np.array(np.arange(-10, 10, 0.01))
y_values = np.array(Gaussian(real_mean, real_fwhm, real_height)(x_axis))
noisy_y_values = np.array(AddNoise(y_values, x_axis, rms))

plt.figure()
plt.plot(x_axis, noisy_y_values, label = 'with noise', color = 'black')
plt.plot(x_axis, y_values, label = 'signal', color = 'blue', linewidth = 4)
plt.legend(loc = 3)
plt.show()


###########################################
#                                         #
#        Use Emcee to fit Gaussian        #
#                                         #
###########################################

def lnprior(x):
	'''
	This will restrict the range of the parameters Emcee will attempt
	'''
	(mean, fwhm, height) = x
	if -5.0 < mean < 5.0 and 0.0 < fwhm < 5.0 and -100.0 < height < 100.0:
		return 0.0
	else:
		return -np.inf

def lnprob(x, x_axis, noisy_y_values):
	'''
	This is the function that Emcee will use to test if it's guesses are 'good'. In statistical terms it's the log probability,
	which is the logarithm of the probability that the model Emcee is proposing is 'correct'. For practical purposes though it's 
	just a function that returns a negative value, and that value is closer to zero for a 'better' set of input values. Emcee 
	will try to maximise the result of this function.
	The argument 'x' is a position vector in parameter space corresponding to a 'guess' of the function parameters. After that
	are any other values needed to evaluate the test function. If you're fitting data then your data should be in here.
	'''
	# apply prior
	if np.isfinite(lnprior(x)):
		# Emcee will try different values within the vector x, here you tell it what those values represent
		(mean, fwhm, height) = x

		# Make a Gaussian out of these test values
		test_Gaussian = Gaussian(mean, fwhm, height)(x_axis)

		# Compare this test Gaussian to the 'real' Gaussian (i.e. the noisy data)
		error = test_Gaussian - noisy_y_values

		# We need to return a single value that is negative, and closer to 0 if the fit is 'good'. So rather than an array of errors
		#	we'll find 0 - root mean square of errors
		rms_error = 0 - math.sqrt(np.nanmean(error**2.0))

		return rms_error
	else:
		return -np.inf


# Number of variables we're trying to find. This determines the number of elements in 'x' to be used in the function 'lnprob'
ndim = 3

# Emcee can try many possible soulutions in parallel to avoid getting 'stuck' in a local maximum. For a simple model this doesn't
#	need to be high
nwalkers = 20

# Emcee will move towards 'better' solutions in parameter space at every iteration. More iterations should lead to a more 
#	accurate result, within reason
niterations = 400

# p0 is an initial guess. If you expect your parameters to be of the order 1 then this is fine. Otherwise multiply by a suitable 
#	value or set the array manually.
p0 = [np.random.rand(ndim) for i in range(nwalkers)]

# The sampler need to know how many walkers to use (nwalkers), how many test parameters to create (ndim), how to test those 
#	parameters (lnprob), and what other values need to go into the test function (args)
sampler = emcee.EnsembleSampler(nwalkers, ndim, lnprob, args=[x_axis, noisy_y_values])

# We then run Emcee, telling it the initial guesses and how many iterations to perform. 
sampler.run_mcmc(p0, niterations)



##########################################
#                                        #
#             Access Results             #
#                                        #
##########################################

'''
After running Emcee, the 'sampler' object will contain your results. For more info see http://dfm.io/emcee/current/api/

Here we'll only look at two:

sampler.lnprobability gives an array of shape (nwalkers, niterations). These are the outputs of the lnprob function
sampler.chain gives an array of the vectors 'x' in the same shape as the sampler.lnprobability array

The maximum value within sampler.lnprobability will correspond to the best set of variables in sampler.chain
'''


# identify lowest error result. This is max rather than min because lnprob returned 0 - error
lowest_error = np.nanmax(sampler.lnprobability)

# identify which argument has the lowest error as this will let us find the best parameters. This might be an array if more 
#	than one of the walkers found the solution or if there are multiple solutions. I'll assume there's one
lowest_error_arg = np.argwhere(sampler.lnprobability == lowest_error)
# better to use np.argsort

plt.figure()
plt.scatter(sampler.flatlnprobability, sampler.flatchain[:, 0], label = 'mean', color = 'black')
plt.scatter(sampler.flatlnprobability, sampler.flatchain[:, 1], label = 'fwhm', color = 'blue')
plt.scatter(sampler.flatlnprobability, sampler.flatchain[:, 2], label = 'height', color = 'green')
plt.xlabel('lnprobability')
plt.xlim(-5, 0)
plt.ylim(-5, 5)
plt.legend(loc = 3)
plt.show()


mean_output = sampler.chain[lowest_error_arg[0][0]][lowest_error_arg[0][1]][0]
fwhm_output = sampler.chain[lowest_error_arg[0][0]][lowest_error_arg[0][1]][1]
height_output = sampler.chain[lowest_error_arg[0][0]][lowest_error_arg[0][1]][2]

plt.figure()
plt.plot(x_axis, noisy_y_values, label = 'with noise', color = 'black')
plt.plot(x_axis, y_values, label = 'signal', color = 'blue', linewidth = 4)
plt.plot(x_axis, Gaussian(mean_output, fwhm_output, height_output)(x_axis), label = 'fit', color = 'red', linewidth = 4, 
			linestyle = '--')
plt.legend(loc = 3)
plt.show()

print '################ Results ################'
print '# mean:      ' + str(mean_output) + '\t\t#'
print '# fwhm:      ' + str(fwhm_output) + '\t\t#'
print '# height:    ' + str(height_output) + '\t\t#'
print '# rms error: ' + str(0 - lowest_error) + '\t\t#'
print '#########################################'





