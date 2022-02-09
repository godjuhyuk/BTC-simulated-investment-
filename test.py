import requests

class Wallet:

    def __init__(self, value):
        self.wallet = value
        self.coin_wallet = {}
    def setWallet(self,value):
        self.wallet = value
    def setCoinWallet(self,coin_name, how_much):
        self.coin_wallet[coin_name] = how_much

    def getWallet(self):
        return self.wallet
    def getCoinWallet(self):
        return self.coin_wallet

    def getCoinWallet(self,coin_name):
        return self.coin_wallet[coin_name]

raw_data = requests.get("https://api.bithumb.com/public/ticker/ALL_KRW")
data = raw_data.json()
#데이터 긁어오면 html에 뿌려주기

mywallet = Wallet(100000000)

def bid(coin_name,how_much):
    coin_data = requests.get("https://api.bithumb.com/public/ticker/"+coin_name+"_KRW")
    data = coin_data.json()
    # print(data)
    # my_coin_wallet[coin_name] += how_much / int(data['data']['closing_price'])
    mywallet.setWallet(Wallet.getWallet(mywallet)-how_much)
    mywallet.setCoinWallet(coin_name,how_much / int(data['data']['closing_price']))
    print(Wallet.getWallet(mywallet))
    

def check(coin_name):
    coin_data = requests.get("https://api.bithumb.com/public/ticker/"+coin_name+"_KRW")
    data = coin_data.json()
    print('현재 보유중인 '+coin_name+ '의 가격은 ' + str( mywallet.getCoinWallet(coin_name) * float(data['data']['closing_price']))+ '입니다. ')
    print('현재 코인 보유량은 '+ str(mywallet.getCoinWallet(coin_name))+ ' 입니다.' )

bid('BTC',20000000)
check('BTC')
