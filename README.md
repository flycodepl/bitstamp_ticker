bitstamp_ticker
===============
#Depending:
```
sudo pip install git+git://github.com/kmadac/bitstamp-python-client.git
```

#Get api keys:
Go to bitstamp.net -> Account -> Security -> API Access -> New API Key -> Check 'Account balance' -> Generate key -> Activate

#Settings:
You must set:
user_id
api_key
api_secret
deposit - your deposit (in your currency)
exchange - exchange from USD to your currency

#Example output:
540.00 * 0.395375=213.50=647.98(-84.01)

540.00   - current exchange BTC to USD
0.395375 - BTC balance
231.50   - balance in USD
647.90   - balance in PLN
-84.01   - your profit
