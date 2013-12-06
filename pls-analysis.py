import numpy as np 

from sklearn.pls import PLSCanonical, PLSRegression, CCA


READ = 'rU'
WRITE = 'wb'
directory = json.load(open('directory.json',READ))

def convert(item):
	item = item.strip()
	if item == 'M' or item == 'vps' or item == 'ICU' or item == 'LF' or item == 'L':
		return -1
	elif item == 'F' or item == 'evd' or item == 'OR' or item == 'RF' or item == 'R':
		return 1
	elif item == 'om' or item == 'ED' or item == 'LT':
		return 0
	elif item == 'LO' or item == 'AG':
		return -2
	elif item == 'RO':
		return 2
	else:
		return item

#Could all this be done with a GNUplot script?
with open('../Data/variables',READ) as f:
	vois = [x.rstrip('\t\n') for x in f.readlines()]

translation = json.load(open('../Data/better-names.json',READ))

cols = set(range(35))
bad_cols = set([0,1,2,12,13,29,30])
good_cols = list(cols-bad_cols)

conversion = dict(zip(range(35),vois))

labels = [translation[conversion[col]] for col in good_cols if col !=9]
with open(directory['data'],READ) as fid:
	reader = csv.reader(fid)
	reader.next()

	data =np.array(filter(lambda row: '' not in row and 'NA' not in row and '?' not in row,
			[[convert(row[i]) for i in good_cols] for row in reader])).astype(float)
	loc = data[:,9]
	tumor = data[:,4]
	data = (data- data.min(axis=0))/(data.max(axis=0)-data.min(axis=0))
	y = data[:,7]
	x = np.delete(data,7,1)
