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
        #url = 'http://stat.columbia.edu/~rachel/datasets/nyt'+str(i)+'.csv'
        url = 'nyt'+str(i)+'.csv'
        print 'Retrieving...', url
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

df = get_nytimes_datasets(1)
#df['CTR'] = df[['Clicks','Impressions']].apply(CTR)
df2= df[["Age","Gender","Signed_In","Clicks","Impressions"]].groupby(["Age","Gender","Signed_In"]).apply(CTR)
print df2

df2.to_csv('nytimes_aggregation.csv', header=True)