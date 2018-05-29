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
# Coinmarketcap.com
#
# Docs: https://coinmarketcap.com/api/

import requests, json, time
import pandas as pd
import urllib3

def main():

    # Show raw JSON ticker data
    url = 'https://api.coinmarketcap.com/v1/ticker/'
    http = urllib3.PoolManager()
    tickers_json = http.request('GET', url)
    #print(tickers_json.data)

    # Convert to DataFrame and show head
    print('Get universe of tickers')
    df = pd.read_json('https://api.coinmarketcap.com/v1/ticker/')
    print(df.head())
    print(df.info())

    # Sort and iterate through
    df = df.sort_values(by=['symbol'])
    for i, r in df.iterrows():
        print(i,r['symbol'],r['price_usd'])
    
    # Select specific cryptos
    selections = ['ETH','BTC']
    df = df[df['symbol'].isin(selections)]
    print(df[['id','price_usd']])

    # Pseudo-streaming of LTC price, CTRL-C to exit
    print("Stream litecoin price")
    for n in range(0,2):
        df = pd.read_json('https://api.coinmarketcap.com/v1/ticker/litecoin')
        print(df['price_usd'])
        time.sleep(15)
