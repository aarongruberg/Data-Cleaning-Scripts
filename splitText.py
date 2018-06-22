### CLEAN TEXT IN COLUMNS SUCH AS COMPANY NAMES AND COUNTRY COODES

import pandas as pd 
import sys  

# Changed default string encoding from 'ascii' to 'utf8'
reload(sys)  
sys.setdefaultencoding('utf8')

# Read input list file
f = 'Enterprise_List_for_Lead_Gen.csv'
df = pd.read_csv(f)

# Drop rows where all values are NaN
df = df.dropna(how='all')
#df = df.head(10)

#----------------------------------------------------------------------------------------------------

# Clean 'Country' column, split on '-'

df['Country'] = df['Country'].str.split('-', 1).str[1]

#----------------------------------------------------------------------------------------------------

# Split data in 'address column' into 'Street Address' and 'City' columns in input list file

#df['City'], df['Street Address'] = df['Street Address'].str.split('-', 1).str

#----------------------------------------------------------------------------------------------------

df.to_csv('Enterprise_List_for_Lead_Gen_Cleaned.csv', index = False)

