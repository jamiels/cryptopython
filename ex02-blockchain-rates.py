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
# Rates
#
# Docs: https://github.com/blockchain/api-v1-client-python/blob/master/docs/exchangerates.md

from blockchain import exchangerates as er

# Get a list of currency symbols
currency_symbols = er.get_ticker()

# Print list of symbols
for c in currency_symbols:
    print (c)

# Cost of BTC in currency
for c in currency_symbols:
    print(c," :", currency_symbols[c].p15min)

# Cost of currency in BTC
for c in currency_symbols:
    print("1 BTC :", 1/ currency_symbols[c].p15min, c)
    
# Direct look up
cad_base_btc = er.to_btc('CAD',5000)
print('1 CAD costs',cad_base_btc,'BTCs')

