
# Blockchain.info Block Exploration


# Docs: https://github.com/blockchain/api-v1-client-python/blob/master/docs/statistics.md

from blockchain import statistics as statistics

def main():
    s = statistics.get()

    print("Trade Volume:", s.trade_volume_btc)
    print("# of Tx last 24 hours: ", s.number_of_transactions)
    print("Total BTC Sent last 24 hours: ", '{:,.2f}'.format(satoshis_to_btc(s.total_btc_sent)))
    print("Miners Revenue USD last 24 hours", '${:,.2f}'.format(s.miners_revenue_usd)  )
    #print(s.total_fees_btc)


def satoshis_to_btc(satoshi):
    return satoshi / 100000000 # one one hundred millionth


if __name__ == "__main__":
    main()