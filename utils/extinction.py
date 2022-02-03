import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pickle
import sfdmap
import extinction
from tqdm import tqdm
from astropy.table import Table
import glob

def correction(data, save=True):
	Base_Filters   = ['u', 'J0378', 'J0395', 'J0410', 'J0430', 'g', 'J0515', 'r', 'J0660', 'i', 'J0861', 'z']
	Features_SPLUS = [filt+'_'+'iso' for filt in Base_Filters]
	Extinct_SPLUS  = [filt+'_ext' for filt in Base_Filters]
	m = sfdmap.SFDMap('/home/mariko/Research/Projects/classify_splus/utils/dustmaps')
	EBV = m.ebv(data.RA, data.DEC)

	# Obtaining Av for each position
	AV  = m.ebv(data.RA, data.DEC)*3.1

	# Estimating extinction for each lambda
	# Extinction law: Cardelli, Clayton & Mathis.
	Lambdas = np.array([3536, 3770, 3940, 4094, 4292, 4751, 5133, 6258, 6614, 7690, 8611, 8831]).astype(np.float)

	Extinctions = []
	for i in range(len(AV)):
	    Extinctions.append(extinction.ccm89(Lambdas, AV[i], 3.1))

	Extinction_DF = pd.DataFrame(Extinctions, columns=Extinct_SPLUS)
	data = data.reset_index(drop=True)

	for i in range(len(Features_SPLUS)):
	    data[Features_SPLUS[i]] = data[Features_SPLUS[i]].reset_index(drop=True) - Extinction_DF[Extinct_SPLUS[i]]
	    data.loc[data[Features_SPLUS[i]]>90,Features_SPLUS[i]] = 99

	if save:
		data.to_csv(file.split('/')[-1], sep="," , index=False)

	return data