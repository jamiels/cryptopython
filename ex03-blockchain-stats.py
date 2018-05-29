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
# Block Exploration
#
# Docs: https://github.com/blockchain/api-v1-client-python/blob/master/docs/statistics.md

from blockchain import statistics as stats

def main():
    s = stats.get()

    # Print some stats
    print('Total blocks ', s.total_blocks)
    print("Trade Volume:", s.trade_volume_btc)
    print("# of Tx last 24 hours: ", s.number_of_transactions)
    print("Total BTC Sent last 24 hours: ", '{:,.2f}'.format(satoshis_to_btc(s.total_btc_sent)))
    print("Miners Revenue USD last 24 hours", '${:,.2f}'.format(s.miners_revenue_usd)  )

    # http://bitcoin.sipa.be/
    print("Hash rate:", s.hash_rate)
    print("Difficult", s.difficulty)

def satoshis_to_btc(satoshi):
    return satoshi / 100000000 # one one hundred millionth

if __name__ == "__main__":
    main()
