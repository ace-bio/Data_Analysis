'''This is a python code that aims to generate a csv table
that generate sample labeling ids. The row contains the number
of samples,the columns are the various tests/procedures carried
out on the samples'''

# import dependencies
import pandas as pd

# create an empty list for all the columns
Col1 = []
Col2 = []
Col3 = []
Col4 = []
Col5 = []
Col6 = []
Col7 = []
Col8 = []

#using  a for loop, append labels(sample no & Alphabets) to each key list
for x in range(1,200):
    Col1.append(str(x)+"A")
    Col2.append(str(x)+"B")
    Col3.append(str(x)+"C")
    Col4.append(str(x)+"D")
    Col5.append(str(x)+"E")
    Col6.append(str(x)+"F")
    Col7.append(str(x)+"G")
    Col8.append(str(x)+"H")

#create a dictionary values list using the column list variables
values = [Col1,Col2,Col3,Col4,Col5,Col6,Col7,Col8]

# create a list of keys, this is the column names
keys = ['BPW', 'RVS', 'seleniteF', 'RVS_SSA', 'RVS_XLD', 'SF_SSA', 'SF_XLD', 'MH']

# convert keys and values list to a dictionary
my_dict = dict(zip(keys,values))

# convert dictionary to a dataframe
df = pd.DataFrame.from_dict(my_dict, orient='index')
#Transpose the dictionary
df1 = pd.DataFrame(data=df).T

# save df1 as csv
df1.to_csv('Experimental labels.csv', sep=',', index = False)
