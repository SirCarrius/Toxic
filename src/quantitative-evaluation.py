import numpy as np

def confusion_matrix(actual, predicted):
	"""
		Assume that actual and predicted are two numpy arrays where the
		ith position in each refers to the classification of 
		the same item
	"""
	assert len(actual) == len(predicted)
	conf_mat = np.zeros((len(actual),len(actual)))

	labels = np.unique(actual)

	for i,one in enumerate(labels):
		for j,two in enumerate(labels):
			
			conf_mat[i,j] = len(set(accurate == one) 
							   & set(predicted == two))

	return conf_mat