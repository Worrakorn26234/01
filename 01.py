from songline import Sendline
token = 'vqCTCOy5oJv7QV4v4P69uqzqj60lJ4F4I74eimsNcEF'
messenger = Sendline(token)

balance = 1000
Fix_value = 1000
BTC_value = 1000

if BTC_value < Fix_value:
    amount = Fix_value - BTC_value
    print(messenger.sendtext('Buy BTC ' + str(amount)))

elif BTC_value > Fix_value:
    amount = BTC_value - Fix_value
    print(messenger.sendtext('Sell BTC ' + str(amount)))

else:
    print(messenger.sendtext('Do notihng'))