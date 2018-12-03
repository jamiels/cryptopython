from flask import Flask
from flask import request
from flask import redirect
from flask import render_template
from CoinTrader import CoinTrader
import pandas as pd

app = Flask(__name__)
ct = CoinTrader()
ct.trade(5,'eth')


# $env:FLASK_DEBUG=1

@app.route('/process',methods=['POST'])
def process_order():
    qty = int(request.form['qty'])
    asset = request.form['asset']
    ct.trade(qty,asset)
    return redirect('/blotter')

@app.route('/')
def index():
    return render_template('main.html',assets=ct.get_assets())

@app.route('/pl')
def pl():
    print(pl)
    return render_template('pl.html',pl=ct.get_pl())

@app.route('/blotter')
def blotter():
    print(blotter)
    return render_template('blotter.html',blotter=ct.get_blotter())

@app.route('/trades')
def trades():
    asset = request.args.get('asset')
    trades = ct.get_recent_trades(asset+'-usd')
    return render_template('trades.html',trades=trades)

@app.route('/lob')
def lob():
    asset = request.args.get('asset')
    print('asset is:',asset)
    lob = ct.get_limit_order_book(asset+'-usd')
    return render_template('lob.html',lob=lob)
