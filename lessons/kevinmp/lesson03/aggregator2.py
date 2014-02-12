#!/usr/bin/env python
from __future__ import division
import pandas as pd
import numpy

def get_nytimes_datasets(n):
    """
    request NYT datasets
    @param int n     number of CSVs to obtain
    @return list      list of CSVs
    """
    assert n < 31
    df = pd.DataFrame()
    for i in range(1,n+1):
	# files already curl-ed to local so no need to dl on the fly
        #url = 'http://stat.columbia.edu/~rachel/datasets/nyt'+str(i)+'.csv'
        url = 'nyt'+str(i)+'.csv'
	print 'Reading...', url
        csv = pd.read_csv(url)
        print 'Obtained', len(csv), 'records'
        df = df.append(csv)
    return df

def ratio(x,y):
    if y != 0:
        return x/y
    else:
        return 0

def CTR(df):
    return  (sum(df["Clicks"])/sum(df["Impressions"]))

# just load 1 data file in this example
df = get_nytimes_datasets(1)

# group by and apply calcs returns as Serial
df=df[["Age","Gender","Signed_In","Clicks","Impressions"]].groupby(["Age","Gender","Signed_In"]).apply(CTR)

# throw the serial back into a dataframe
df2 = pd.DataFrame(df).reset_index()

# add in header for CTR column
df2.rename(columns={0:'CTR'}, inplace=True)

# write out CSV file with header but no index
df2.to_csv('nytimes_aggregation2.csv', header=True, index=False)
