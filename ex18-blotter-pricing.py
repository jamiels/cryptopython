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
# Blotter & Pricing
#
# Docs: https://docs.gdax.com

import requests, io, time
import pandas as pd
import datetime as dt


def main():    
    blotter, col_names = initialize_blotter()
    
    bid, ask = get_price("eth-usd")
    print("bid ", bid, " ask", ask)
    data = pd.DataFrame([[dt.datetime.now(),'ETH',1.223, ask]] ,columns=col_names)
    blotter = blotter.append(data, ignore_index=True)
    print(blotter)


def get_price(pair):
    df = load('https://api.gdax.com/products/'+pair+'/book',printout=False)
    ask = df.iloc[0]['asks'][0]
    bid = df.iloc[0]['bids'][0]
    return float(bid), float(ask)

# Initialize a new blotter
  
def initialize_blotter():
    col_names = ['Timestamp','Pair','Quantity','Executed Price']
    return pd.DataFrame(columns=col_names), col_names

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
