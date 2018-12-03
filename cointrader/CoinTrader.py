import pandas as pd
import requests
import time
import datetime as dt

class CoinTrader:
    def __init__(self,assets=['eth','btc'],debug=False):
        self.__assets = assets
        self.__pl = self.__initialize_pl()
        self.__blotter = self.__initialize_blotter()
        self.__debug = debug

    def get_assets(self):
        return self.__assets.copy()
        
    def print(self):
        print(self.__pl)
        print(self.__blotter)

    def get_limit_order_book(self,asset):
        return self.__load('https://api.gdax.com/products/'+asset+'/book?level=2',printout=True)

    def __initialize_pl(self):
        col_names = ['Asset', 'Position', 'VWAP', 'UPL', 'RPL']
        pl = pd.DataFrame(columns=col_names)
        for p in self.__assets:
            data = pd.DataFrame([[p, 0, 0, 0, 0]], columns=col_names)
            pl = pl.append(data, ignore_index=True)
        return pl
    
    def get_blotter(self):
        return self.__blotter.copy()
    def get_pl(self):
        return self.__pl.copy()

    def trade(self,qty, asset):
        bid, ask = self.__get_price(asset)
        if qty > 0:
            price = ask
        else:
            price = bid
        data = pd.DataFrame([[dt.datetime.now(), asset, qty, price]], columns=[
                            'Timestamp', 'Asset', 'Quantity', 'Executed Price'])
        self.__blotter = self.__blotter.append(data, ignore_index=True)

    def __update_pl(self,symbol,qty,price):
        current_qty = self.__pl.at[symbol,'Quantity']
        current_vwap = self.__pl.at[symbol,'VWAP']

        new_qty = current_qty + qty
        self.__pl.at[symbol,'Quantity'] = new_qty
        if new_qty == 0:
            new_vwap = 0
        else:
            new_vwap = self.__calc_vwap(current_qty,current_vwap,qty,price)
        
        self.__pl.at[symbol,'UPL'] = (new_qty * price) - (new_qty * new_vwap)
        
        if qty > 0: # buy
            self.__pl.at[symbol,'VWAP'] = new_vwap
        elif qty < 0: #sell
            rpl = self.__pl.at[symbol,'RPL']
            abs_qty = abs(qty)
            net = (abs_qty * price) - (abs_qty * current_vwap)
            self.__pl.at[symbol,'RPL'] = rpl + net
        return pl, new_vwap


    def __calc_vwap(self,current_qty, current_vwap, qty, price):
        current_dollar = current_qty * current_vwap
        new_dollar = current_dollar + (qty * price)
        new_qty = current_qty + qty
        new_vwap = new_dollar / new_qty
        return new_vwap

    def get_recent_trades(self,asset):
        return self.__load('https://api.gdax.com/products/' + asset + '/trades',printout=self.__debug)

    def __get_price(self,asset):
        df = self.__load('https://api.gdax.com/products/'+asset+'-usd/book', printout=self.__debug)
        ask = df.iloc[0]['asks'][0]
        bid = df.iloc[0]['bids'][0]
        return float(bid), float(ask)
    
    def __initialize_blotter(self):
        col_names = ['Timestamp', 'Asset', 'Quantity', 'Executed Price']
        return pd.DataFrame(columns=col_names)
    
    def __load(self,url, printout=False, delay=0, remove_bottom_rows=0, remove_columns=[]):
        time.sleep(delay)
        header = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}
        r = requests.get(url, headers=header)
        df = pd.read_json(r.text)

        if remove_bottom_rows > 0:
            df.drop(df.tail(remove_bottom_rows).index, inplace=True)
        df.drop(columns=remove_columns, axis=1)
        df = df.dropna(axis=1)
        if printout:
            print(df)
        return df

    