from time import sleep
import bitstamp.client as btc

while True:
    i=0
    user_id='xxx'
    api_key='xxx'
    api_secret='xxx'
    deposit=500 # in PLN
    exchange=3.035 # USD to PLN

    btc_trading = btc.trading(username=user_id, key=api_key, secret=api_secret)
    account_info = btc_trading.account_balance()
    btc_public = btc.public()

    for i in range(0,100):
        info = btc_public.ticker()

        last_price = float(info.get('last'))
        amount_btc = float(account_info.get('btc_balance'))
        amount_in_usd = amount_btc*last_price
        amount_in_pln = amount_in_usd*exchange
        profit = (amount_btc*last_price*exchange)-deposit

        text_info = "%.2f * %f=%.2f=%.2f(%.2f)" % (last_price, amount_btc, amount_in_usd, amount_in_pln, profit)
        print text_info
        print account_info

        fs = open('/tmp/btcinfo', 'w')
        fs.write(text_info)
        fs.close()
        sleep(5)


