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
# GDAX Order Book
#
# Docs: https://docs.gdax.com

import requests
import io
import time
import pandas as pd

# 1 - Display and explain plotly
# Learn about API authentication here: https://plot.ly/nodejs/getting-started
# Find your api_key here: https://plot.ly/settings/api


def main():
    # Show best bid / ask for Eth
    df = load('https://api.gdax.com/products/eth-usd/book', printout=True)

    print(df['asks'])
    # can turn into a list, but dont need to, see ex12.3
    best_ask = df['asks'].tolist()
    print('Best ask price', best_ask[0][0])
    print('Best ask qty available', best_ask[0][1])
    print('Best ask parties', best_ask[0][2])

    best_bid = df['bids'].tolist()
    print('Best ask price', best_bid[0][0])
    print('Best ask qty available', best_bid[0][1])
    print('Best ask parties', best_bid[0][2])

    spread = float(best_ask[0][0]) - float(best_bid[0][0])
    print('Spread', spread)

# Load function


def load(url, printout=False, delay=0, remove_bottom_rows=0, remove_columns=[]):
    time.sleep(delay)
    header = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}
    r = requests.get(url, headers=header)
    df = pd.read_json(r.text)

    if remove_bottom_rows > 0:
        df.drop(df.tail(remove_bottom_rows).index, inplace=True)
    df.drop(columns=remove_columns, axis=1)
    df = df.dropna(axis=1)
    if printout:
        print(df)
    return df


if __name__ == "__main__":
    main()
