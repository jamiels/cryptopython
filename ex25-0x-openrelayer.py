import requests, time, json
import pandas as pd

# https://api.openrelay.xyz/v0/orders

def main():
    r = requests.get('https://api.openrelay.xyz/v0/orders')
    #print(r.text)
    order_book = json.loads(r.text)
    # for o in order_book:
    #     for k,v in o.items():
    #         print(k,v)

    for k,v in order_book[0].items():
        print(k,v)

if __name__ == "__main__":
    main()