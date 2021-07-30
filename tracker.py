# это код который парсит инфу
import requests


def get_prices():
    try:
        coins = ["BTC", "ETH", "DOGE", "LTC", "ADA", "VTC"]
        crypto_data = requests.get(
            "https://min-api.cryptocompare.com/data/pricemultifull?fsyms={}&tsyms=USD".format(",".join(coins))).json()["RAW"]

        data = {}
        for i in crypto_data:
            data[i] = {
                "coin": i,
                "price": crypto_data[i]["USD"]["PRICE"],
                "change_day": crypto_data[i]["USD"]["CHANGEPCT24HOUR"],
                "change_hour": crypto_data[i]["USD"]["CHANGEPCTHOUR"]
            }

        return data    

    except Exception as err:
        print(err)

def get_prices_kompa():
    try:
    
        compani = ["TSLA","AMZN","AAPL","NEM","NEE","AVGO"]
        compani_data = requests.get(
            "https://query1.finance.yahoo.com/v7/finance/quote?symbols={}".format(",".join(compani))).json()["quoteResponse"]

        data = {}
        # print(compani_data['result'])
        for i in compani_data['result']:
            data[i["longName"]] = {
                'price': i['regularMarketPrice'],
                'change': i['regularMarketChange'],
                'percent': i['regularMarketChangePercent']
            }
            # data2[i] = {
            #     "compani": i["result"]["0"]["longName"],
            #     "price": compani_data["result"]["0"]["postMarketPrice"],
            #     "change_day": compani_data["result"]["0"]["twoHundredDayAverageChangePercent"],
            #     #"change_hour": compani_data[i]["USD"]["CHANGEPCTHOUR"]
            # }

        return data
    except Exception as err:
            print(err)
            
def get_prices_curr():
    try:
    
        curr = ["RUBUSD=X","EURUSD=X","BYNUSD=X","UAHUSD=X","PLNUSD=X","KZTUSD=X"]
        curr_data = requests.get(
            "https://query1.finance.yahoo.com/v7/finance/quote?symbols={}".format(",".join(curr))).json()["quoteResponse"]

        data = {}
        # print(compani_data['result'])
        for i in curr_data['result']:
            data[i["shortName"]] = {
                'price': i['regularMarketPrice'],
                'change': i['regularMarketChange'],
                'percent': i['regularMarketChangePercent']
            }
            # data2[i] = {
            #     "compani": i["result"]["0"]["longName"],
            #     "price": compani_data["result"]["0"]["postMarketPrice"],
            #     "change_day": compani_data["result"]["0"]["twoHundredDayAverageChangePercent"],
            #     #"change_hour": compani_data[i]["USD"]["CHANGEPCTHOUR"]
            # }

        return data
    except Exception as err:
            print(err)
#print(get_prices_kompa())
#print(get_prices())
# это код который парсит инфу