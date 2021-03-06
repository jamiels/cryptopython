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
# Blotter
#
# Docs: https://docs.gdax.com

import requests, io, time
import pandas as pd
import datetime as dt

def main():    
    blotter, col_names = initialize_blotter()
    
    # Add some dummy data
    data = pd.DataFrame([[dt.datetime.now(),'ETH',1.223,541.33]] ,columns=col_names)
    blotter = blotter.append(data, ignore_index=True)

    data = pd.DataFrame([[dt.datetime.now(),'ETH',2.623,561.33]] ,columns=col_names)
    blotter = blotter.append(data, ignore_index=True)

    data = pd.DataFrame([[dt.datetime.now(),'ETH',2.723,571.33]] ,columns=col_names)
    blotter = blotter.append(data, ignore_index=True)
    
    data = pd.DataFrame([[dt.datetime.now(),'ETH',3.43, 521.33]] ,columns=col_names)
    blotter = blotter.append(data, ignore_index=True)

    print(blotter)

# Initialize a new blotter
def initialize_blotter():
    col_names = ['Timestamp','Pair','Quantity','Executed Price']
    return pd.DataFrame(columns=col_names), col_names

if __name__ == "__main__":
    main()
