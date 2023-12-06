'''This is a python code that aims to generate a csv table
that generate sample labeling ids. The row contains the number
of samples,the columns are the various tests/procedures carried
out on the samples'''

# import dependencies
import pandas as pd

# create an empty list for all the columns
BPW = []
RVS = []
seleniteF = []
RVS_SSA = []
RVS_XLD = []
SF_SSA = []
SF_XLD = []
MH = []

#using  a for loop, append labels(sample no & Alphabets) to each key list
for x in range(1,200):
    BPW.append(str(x)+"A")
    RVS.append(str(x)+"B")
    seleniteF.append(str(x)+"C")
    RVS_SSA.append(str(x)+"D")
    RVS_XLD.append(str(x)+"E")
    SF_SSA.append(str(x)+"F")
    SF_XLD.append(str(x)+"G")
    MH.append(str(x)+"H")

#create a dictionary values list using the column list variables
values = [BPW,RVS,seleniteF,RVS_SSA,RVS_XLD,SF_SSA,SF_XLD, MH]

# create a list of keys, this is the column names
keys = ['BPW', 'RVS', 'seleniteF', 'RVS_SSA', 'RVS_XLD', 'SF_SSA', 'SF_XLD', 'MH']

# convert keys and values list to a dictionary
my_dict = dict(zip(keys,values))

# convert dictionary to a dataframe
df = pd.DataFrame.from_dict(my_dict, orient='index')
#Transpose the dictionary
df1 = pd.DataFrame(data=df).T

df1.head(10)
# save df1 as csv
df1.to_csv('Experimental labels.csv', sep=',', index = False)
