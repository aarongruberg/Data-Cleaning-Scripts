import pandas as pd
import numpy as np
import sys  

# Changed default string encoding from 'ascii' to 'utf8'
reload(sys)  
sys.setdefaultencoding('utf8')

f1 = 'DME List with Domains.csv'
f2 = 'Q3 Stock $50K above(1).csv'

DME_df = pd.read_csv(f1, skiprows=None)
Q3_df = pd.read_csv(f2, skiprows=None)

#Q3_df['Sub Standardize ID'] = Q3_df['Sub Standardize ID'].astype(str)
#print type(Q3_df['Sub Standardize ID'].values)

def duplicates(subID):
	#print type(subID)
	#print type(s)
	if subID != '--':

		subID = int(subID)

		if subID in Q3_df['Sub Standardize ID'].values:
			return 'duplicate'
		else:
			return subID


def remove_duplicates(subID):

	DME_df['Sub Id'] = subID.apply(duplicates)

	return DME_df


DME_df = remove_duplicates(DME_df['Sub Id'])

DME_df.to_csv('DME List with Domains Removed Duplicates.csv', index = False)


