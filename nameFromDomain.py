### GET AND CLEAN COMPANY NAME FROM DOMAINS

# This can be used to get company names for input list match file
# before it is loaded into the platform.

import pandas as pd 
import math

# Read input list file
f = 'Synopsys_EMEA_List Match.csv'
df = pd.read_csv(f)

# Drop rows where all values are NaN
df = df.dropna(how='all')

#df = df.head(10)

#-------------------------------------------------------------------------------------------------------

def getName(name, domain):

	if type(name) != str:

		if math.isnan(name) == True:

			name = domain.split(".")
			name = name[0]

			if '-' in name:
				name = name.replace('-', ' ')

			return name

	else:

		return name

#--------------------------------------------------------------------------------------------------------

df['Account Name'] = df.apply(lambda x: getName(x['Account Name'], x['Domain']), axis=1)

print df

df.to_csv('Synopsys_EMEA_List_Cleaned.csv', index = False)


