
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
# Ethereum & Matplotlib
#
# Docs: https://etherscan.io/chart/etherprice


import requests
import matplotlib.pyplot as plt
import pandas as pd
import json
import io

def main():
    url = 'https://etherscan.io/chart/etherprice?output=csv'
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    response = requests.get(url, headers=headers)

    # Data from Etherscan.io
    df = pd.read_table(io.StringIO(response.content.decode("utf-8")),sep=",")
    df.dropna()

    # Drop UnixTimeStamp
    df = df.drop(df.columns[1], axis=1)
    
    # Convert Date from str to datetime
    df['Date(UTC)'] = pd.to_datetime(df['Date(UTC)'],format = "%m/%d/%Y")
    
    # Make Date the index
    df.index = df['Date(UTC)']

    # Remove dupe Date
    df = df.drop(df.columns[0], axis=1)
    
    # Plot
    plt.plot(df)
    plt.show()

    

if __name__ == "__main__":
    main()