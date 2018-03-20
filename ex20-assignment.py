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

import requests
import matplotlib.pyplot as plt
import pandas as pd
import json
import io
import time
import datetime as dt

def main():    
    # Initial portfolio size in cash
    funds = 100000000.0
    pairs = ['ethusd','btcusd'] # assume usd base

    # Initialize data structures
    df_blotter = initialize_blotter()
    df_pl = initialize_pl(pairs)
    df_products = get_products()

    # Design a menu a system 
    menu = ('Buy', 'Sell', 'Show Blotter', 'Show PL', 'Quit')
    while True:
        choice = display_menu(menu,exit_option=5)
        if choice == 1:
            # Buy
            print("Choice 1 chosen")
        elif choice == 2:
            print("Choice 2 chosen")
            # Sell
        elif choice == 3:
            view_blotter(df_blotter)
        elif choice == 4:
            view_pl(df_pl)
        # Complete rest

def display_menu(menu,exit_option=-1):
    for m in menu:
        print(menu.index(m)+1,". ",m)
    choice = int(input("Enter choice >> #"))
    if choice==exit_option:
        print("Bye")
        quit()
    return choice

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
        # TODO Recalc UPL
    elif qty < 1: #sell
        # TODO recalc UPL, RPL, position
        print("Insert code handling a sale - recalc UPL,RPL & position")
    return pl

def view_blotter(df_blotter):
    print("---- Trade Blotter")
    print(df_blotter)
    print()


def view_pl(df_pl):
    # TODO Update UPL here
    print("---- PL")
    print(df_pl)
    print()


def get_price(pair):
    df = load('https://api.gdax.com/products/'+pair+'/book',printout=False)
    ask = df.iloc[0]['asks'][0]
    bid = df.iloc[0]['bids'][0]
    return float(bid), float(ask)


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

def get_products():
    df = load('https://api.gdax.com/products',printout=False)
    return df

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