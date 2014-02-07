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

# just load 1 data file in this example
df = get_nytimes_datasets(1)

# group by and sum it - returns a dataframe 
df=df[["Age","Gender","Signed_In","Clicks","Impressions"]].groupby(["Age","Gender","Signed_In"]).sum()

# calculate the CTR. map? we don't need no map.
df["CTR"] = df["Clicks"]/ df["Impressions"]

# drop the unecessary columns
del df["Clicks"]
del df["Impressions"]

#write out CSV file 
df.to_csv('nytimes_aggregation.csv')
