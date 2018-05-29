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
# Ethereum
#
# Docs: https://etherscan.io/chart/etherprice

import requests, io
import pandas as pd

def main():

    # Spoof Mac Chrome browser and request csv
    url = 'https://etherscan.io/chart/etherprice?output=csv'
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    response = requests.get(url, headers=headers)
    
    # Data from Etherscan.io
    # TODO Change to JSON
    df = pd.read_table(io.StringIO(response.content.decode("utf-8")),sep=",")
    print(df.columns)
    print(df.info())
    print(df.head())
    print(df.tail())
    

if __name__ == "__main__":
    main()
