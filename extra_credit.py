import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import datetime as dt
import math
import scipy.optimize as spo

def main():
    pairs = ['ethusd','btcusd']

    # 1. Extract ethusd and btcusd for past 2 years and place into CSV file
    # 2. DataFrame.join() into one DF, set index to date, clean
    # 3. Use NumPy to create equally weight allocs ie. np.full((1,len(pairs)),(1.0/len(pairs)))
    initial_allocs = np.full((1,len(pairs)),(1.0/len(pairs)))
    # 4. Create a function that normalizes data, breaks into allocations, create pct change for each day, find standard deviation and re
    data =  pd.read_csv("") # time series of pairs
    bnds = (())
    for p in pairs:
        bnds = bnds + ((0,1),)

    # Constraints, sum of allocs == 1
    constraints = ({'type': 'eq', 'fun': lambda inputs: 1.0 - np.sum(inputs)})
    # Seek minimum vol
    result = spo.minimize(get_portfolio_vol,initial_allocs,bounds=bnds,constraints=constraints,args=(data,),method='SLSQP',options={'disp':True})
    print(result.x)

def get_portfolio_vol(portfolio,alloc):
    # portfolio has time series of pairs
    portfolio = portfolio * alloc
    portfolio = portfolio.sum(axis=1)
    daily_returns = portfolio.pct_change(1)
    std = daily_returns.std()
    return std

if __name__ == "__main__":
    main()
