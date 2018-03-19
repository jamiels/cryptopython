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

symbols = er.get_ticker()
for k in symbols:
    print(str(k), symbols[k].p15min)


# How much BTC can USD buy?

for d in range(0,100000, 10000):
    print("$",d," = ",er.to_btc('USD',d)," BTC")

