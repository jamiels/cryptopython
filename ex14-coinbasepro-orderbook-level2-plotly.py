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
import plotly
plotly.tools.set_credentials_file(
    username='jamielsheikh', api_key='VNBx3ByJnTptdjg2d0Pc')
import plotly.plotly as py
import plotly.graph_objs as go


def main():

    # Show depth of 50
    df = load('https://api.gdax.com/products/eth-usd/book?level=2')

    bids = []
    asks = []
    prices = []

    for i, r in df.iterrows():
        bids.append(r['bids'][0])
        prices.append(r['bids'][0])
        asks.append(r['asks'][0])
        prices.append(r['asks'][0])

    print(bids)
    print(asks)
    print(prices)

    bids_l2_series = go.Scatter(
        x=bids,
        y=prices
    )

    asks_l2_series = go.Scatter(
        x=asks,
        y=prices
    )

    data = [bids_l2_series, asks_l2_series]
    py.plot(data, filename='l2 bid ask')


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
