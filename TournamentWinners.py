import csv

with open("chessResultsList.csv", encoding="utf-8") as csvfile:
    readCSV = csv.reader(csvfile, delimiter = ',')

#import numpy as np
import pandas as pd
from pandas import Series, DataFrame

chessresult_df = pd.read_csv('chessResultsList.csv')
chessresult_df.head()
#print(chessresult_df)

top = chessresult_df['Pts.'].max()


winners = DataFrame(columns = ('Rk.','Sno','','Name','FED','Rtg','Club/City','Pts.','TB1','TB2','TB3'))


count_row = chessresult_df.shape[0]  # gives number of row 
count_col = chessresult_df.shape[1]  # gives number of col 

#print(top)
#print("No. of rows = ",count_row,"\nNo. of columns = ",count_col)


#print(chessresult_df.loc[chessresult_df['Pts.'] == top])
        
winners = chessresult_df.loc[chessresult_df['Pts.'] == top]

winnername = winners["Name"].to_string(header=False, index=False).replace('\n',',')

print("After round 9,",winnername,"lead the tournament with",top,"points!!")
