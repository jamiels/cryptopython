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
# GDAX Refactorings
#
# Docs: https://docs.gdax.com/

import requests, io, time
import matplotlib.pyplot as plt
import pandas as pd

def main():
    df = load('http://api.coindesk.com/v1/bpi/historical/close.json?start=2018-05-10&end=2018-05-18',remove_bottom_rows=2,remove_columns=['disclaimer'])
    print(df)

def load(url,printout=False,delay=0,remove_bottom_rows=0,remove_columns=[]):
    time.sleep(delay)
    header = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}
    r = requests.get(url, headers=header)
    df = pd.read_json(r.text)


    if remove_bottom_rows > 0:
        df.drop(df.tail(remove_bottom_rows).index,inplace=True)
    df.drop(columns=remove_columns,axis=1,inplace=True)
    df = df.dropna(axis=1)
    if printout:
        print(df)
    return df

if __name__ == "__main__":
    main()
