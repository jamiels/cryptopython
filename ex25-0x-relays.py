import requests, time, json
import pandas as pd

# https://api.openrelay.xyz/v0/orders

def main():
    #r = requests.get('https://api.openrelay.xyz/v0/orders')
    #print(r.text)
    #order_book = json.loads(r.text)
    # for o in order_book:
    #     for k,v in o.items():
    #         print(k,v)

    # https://0xproject.com/portal
    # https://www.ercdex.com/
    # http://api-v2.ledgerdex.com/sra/v2/fee_recipients

    #for k,v in order_book[0].items():
    #    print(k,v)
    
    #df = load('https://api.radarrelay.com/v2/tokens',printout=True)

    

    #  BAT token
    # https://api.radarrelay.com/v2/markets
#     df = load('https://api.radarrelay.com/v2/markets',printout=True) 
#     for r in df.iterrows():
#             print(r[1][3])

    # bat-weth book
    # https://api.radarrelay.com/v2/markets/BAT-WETH/book
    r = requests.get('https://api.radarrelay.com/v2/markets/BAT-WETH/book')
    bat_weth_order_book = json.loads(r.text)

    print(bat_weth_order_book['bids'][0])
    
    #print(bat_weth_order_book)
    # for k,v in bat_weth_order_book.items():
    #  print(k,v)

    for bids in bat_weth_order_book['bids']:
            print(bids['price'])

    
        
        

    # https://github.com/0xProject/standard-relayer-api/blob/master/http/v2.md


def load(url,printout=False,delay=0,remove_bottom_rows=0,remove_columns=[]):
        time.sleep(delay)
        header = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}
        r = requests.get(url, headers=header)
        df = pd.read_json(r.text)

        if remove_bottom_rows > 0:
                df.drop(df.tail(remove_bottom_rows).index,inplace=True)
        df.drop(columns=remove_columns,axis=1)
        df = df.dropna(axis=1)
        if printout:
                print(df)
        return df
if __name__ == "__main__":
    main()