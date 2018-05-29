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


# Build full app

import requests, io, time
import pandas as pd
import datetime as dt


def main(): 

    funds = 100000000.0   
    pairs = ['eth-usd','btc-usd']

    blotter = initialize_blotter()
    pl = initialize_pl(pairs)
    
    blotter, pl = trade(blotter, pl, 1,pairs[0])
    blotter, pl = trade(blotter, pl, 2,pairs[0])
    blotter, pl = trade(blotter, pl, -1,pairs[0])

    print(blotter)
    print(pl)


def trade(blotter,pl,qty,pair):
    bid, ask = get_price(pair)
    if qty > 0:
        price = ask
    else:
        price = bid
    data = pd.DataFrame([[dt.datetime.now(), pair ,qty, price]] ,columns=['Timestamp','Pair','Quantity','Executed Price'])
    blotter = blotter.append(data, ignore_index=True)
    return blotter

def update_pl(pl,pair,qty,price):
    if qty > 0: # buy
        current_qty = pl.at[pair,'Position']
        current_vwap = pl.at[pair,'VWAP']
        new_vwap = calc_vwap(current_qty,current_vwap,qty,price)
        pl.at[pair,'Position'] = current_qty + qty
        pl.at[pair,'VWAP'] = new_vwap
        # TODO Recalc UPL
    elif qty < 1: #sell
        # TODO recalc UPL, RPL, position
        print("Insert code handling a sale - recalc UPL,RPL & position")
    return pl


def calc_vwap(current_qty,current_vwap,qty,price):
    current_dollar = current_qty * current_vwap
    new_dollar = current_dollar + (qty * price)
    new_qty = current_qty + qty
    new_vwap = new_dollar / new_qty
    return new_vwap

# Inititalize PL
def initialize_pl(pairs):
    col_names = ['Pairs','Position','VWAP','UPL','RPL']
    pl = pd.DataFrame(columns=col_names)
    for p in pairs:
        data = pd.DataFrame([[p,0,0,0,0]] ,columns=col_names)
        pl = pl.append(data, ignore_index=True)
    return pl

# Get current pair price
def get_price(pair):
    df = load('https://api.gdax.com/products/'+pair+'/book',printout=False)
    ask = df.iloc[0]['asks'][0]
    bid = df.iloc[0]['bids'][0]
    return float(bid), float(ask)


# Initialize a new blotter  
def initialize_blotter():
    col_names = ['Timestamp','Pair','Quantity','Executed Price']
    return pd.DataFrame(columns=col_names)




# Load function
def load(url,printout=False,delay=0,remove_bottom_rows=0,remove_columns=[]):
    time.sleep(delay)
    header = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}
    r = requests.get(url, headers=header)
    df = pd.read_json(r.text)

    if remove_bottom_rows > 0:
        df.drop(df.tail(remove_bottom_rows).index,inplace=True)
    df.drop(columns=remove_columns,axis=1)
    df = df.dropna(axis=1)
    if printout:
        print(df)
    return df


if __name__ == "__main__":
    main()




# Load function
def load(url,printout=False,delay=0,remove_bottom_rows=0,remove_columns=[]):
    time.sleep(delay)
    header = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}
    r = requests.get(url, headers=header)
    df = pd.read_json(r.text)

    if remove_bottom_rows > 0:
        df.drop(df.tail(remove_bottom_rows).index,inplace=True)
    df.drop(columns=remove_columns,axis=1)
    df = df.dropna(axis=1)
    if printout:
        print(df)
    return df


if __name__ == "__main__":
    main()
