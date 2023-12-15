'''This is a python code that aims to create a csv table
that generate sample labeling ids. The row contains the number
of samples,the columns are the various tests/procedures carried
out on the samples'''

# import dependencies
import pandas as pd

# Takes input of no of columns and rows
No_of_cols = int(input("How many column labels would you work with?"))
No_of_rows = int(input("How many Samples would you work with?"))

# create an empty list for the column names and the lists of the columns value
list_of_cols = []
list_list_col = []

# Populate the list of column name by taking inputs of the column name from users
for col in range(1,No_of_cols+1):
    col = str(input("Enter a short column attribute(please use abbreviations)"))
    list_of_cols.append(col)

# using a nested list create a list of list and append to the lists of list of values
for col in list_of_cols:
    col_list = []
    for no in range(1, No_of_rows+1):
        id = str(no)+col
        col_list.append(id)
    list_list_col.append(col_list)

# create a dictionary
my_dict = dict(zip(list_of_cols, list_list_col))

# convert dictionary to a dataframe
df = pd.DataFrame.from_dict(my_dict, orient='index')
#Transpose the dictionary
df1 = pd.DataFrame(data=df).T

# save df1 as csv
df1.to_csv('Experimental labels.csv', sep=',', index = False)
