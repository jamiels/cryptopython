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
    data = pd.DataFrame([[dt.datetime.now(),'ETH',1.223,'541.33']] ,columns=['Timestamp','Pair','Volume','Executed Price'])
    blotter = blotter.append(data, ignore_index=True)

    data = pd.DataFrame([[dt.datetime.now(),'ETH',2.623,'541.33']] ,columns=['Timestamp','Pair','Volume','Executed Price'])
    blotter = blotter.append(data, ignore_index=True)

    data = pd.DataFrame([[dt.datetime.now(),'ETH',2.723,'541.33']] ,columns=['Timestamp','Pair','Volume','Executed Price'])
    blotter = blotter.append(data, ignore_index=True)
    
    data = pd.DataFrame([[dt.datetime.now(),'ETH',3.43,'541.33']] ,columns=['Timestamp','Pair','Volume','Executed Price'])
    blotter = blotter.append(data, ignore_index=True)

def calc_vwap(pl,qty,price):
    current_qty = pl['Qty']
    current_vwap = pl['VWAP']
    dollar = current_qty * current_vwap
    new_dollar = dollar + (qty * price)
    new_qty = current_qty + qty
    new_vwap = new_dollar / new_qty
    return new_vwap

def initialize_blotter():
    col_names = ['Timestamp','Delta','Symbol','Volume','Executed Price']
    return pd.DataFrame(columns=col_names)

def initialize_pl():
    col_names = ['Pair','Qty','VWAP']
    return pd.DataFrame(columns=col_names)

if __name__ == "__main__":
    main()