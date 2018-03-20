# Copyright Chainhaus
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# VWAP
#
# Docs: https://docs.gdax.com


import requests
import matplotlib.pyplot as plt
import pandas as pd
import json
import io
import time
import datetime as dt

def main():    

    blotter = initialize_blotter()
    pairs = ['ethusd','btcusd'] # assume usd base
    pl = initialize_pl(pairs)

    data = pd.DataFrame([[dt.datetime.now(),'ETH',1.223,541.33]] ,columns=['Timestamp','Pair','Volume','Executed Price'])
    blotter = blotter.append(data, ignore_index=True)
    pl = update_pl(pl,'ethusd',1.223,541.33)
    print(pl)

    data = pd.DataFrame([[dt.datetime.now(),'ETH',2.623,561.33]] ,columns=['Timestamp','Pair','Volume','Executed Price'])
    blotter = blotter.append(data, ignore_index=True)
    pl = update_pl(pl,'ethusd',2.623,561.33)
    print(pl)


    data = pd.DataFrame([[dt.datetime.now(),'ETH',2.723,571.33]] ,columns=['Timestamp','Pair','Volume','Executed Price'])
    blotter = blotter.append(data, ignore_index=True)
    
    data = pd.DataFrame([[dt.datetime.now(),'ETH',3.43, 521.33]] ,columns=['Timestamp','Pair','Volume','Executed Price'])
    blotter = blotter.append(data, ignore_index=True)

def calc_vwap(current_qty,current_vwap,qty,price):
    dollar = current_qty * current_vwap
    new_dollar = dollar + (qty * price)
    new_qty = current_qty + qty
    new_vwap = new_dollar / new_qty
    return new_vwap

def update_pl(pl,pair,qty,price):
    if qty > 0: # buy
        current_qty = pl.at[pair,'Position']
        current_vwap = pl.at[pair,'VWAP']
        new_vwap = calc_vwap(current_qty,current_vwap,qty,price)
        pl.at[pair,'Position'] = current_qty + qty
        pl.at[pair,'VWAP'] = new_vwap

    return pl


def initialize_blotter():
    col_names = ['Timestamp','Pair','Quantity','Executed Price']
    return pd.DataFrame(columns=col_names)


def initialize_pl(pairs):
    col_names = ['Pairs','Position','VWAP','UPL','RPL']
    pl = pd.DataFrame(columns=col_names)
    for p in pairs:
        data = pd.DataFrame([[p,0,0,0,0]] ,columns=col_names)
        pl = pl.append(data, ignore_index=True)
    pl = pl.set_index('Pairs')
    return pl

if __name__ == "__main__":
    main()