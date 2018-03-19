
# Copyright 2018 Chainhaus
# Block Exploration

# Docs - https://github.com/blockchain/api-v1-client-python/blob/master/docs/blockexplorer.md

from blockchain import blockexplorer as be
def main():

    # get latest block (max height)
    latest_block = be.get_latest_block()
    print("Latest height: ",str(latest_block.height))
    print("Latest hash: ",latest_block.hash)


    # hash of the block where laszlo transaction resides
    pizza_block_hash = "00000000152340ca42227603908689183edc47355204e7aca59383b0aaac1fd8"

    # hash of the laszlo tx
    pizza_tx_hash = "a1075db55d416d3ca199f55b6084e2115b9345e16c5cf302fc80e9d5fbf5d48d"

    # get the block
    pizza_block = be.get_block(pizza_block_hash)
    print("The block height for the Laszlo tx ", pizza_block.height)
    
    # get the tx
    pizza_tx = be.get_tx(pizza_tx_hash)
    print("That pizza cost ", satoshis_to_btc(pizza_tx.outputs.pop().value), " BTCs!")

    # get Txs in Laszlo's address
    laszlo_addr = "1XPTgDRhN8RFnzniWCddobD9iKZatrvH4"
    print("Laszlo transaction list for address ", laszlo_addr)
    laszlo_txs = be.get_address(laszlo_addr).transactions
    for t in laszlo_txs:
        for o in t.outputs:
            print(satoshis_to_btc(o.value))
    
def satoshis_to_btc(satoshi):
    return satoshi / 100000000 # one one hundred millionth

if __name__ == "__main__":
    main()