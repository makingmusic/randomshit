import requests
import json

# some standard values
APIKEY = "43AMUJ3X4WU5W63J"
BASEURLGETRATE = "https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&" 
BASEURLSHAREPRICE =  "https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol="
#BASEURLSHAREPRICE =  "https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol=PAYTM.BSE&apikey=43AMUJ3X4WU5W63J"
#URLUSDCAD = "https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=CAD&apikey=" + APIKEY 
#URLUSDINR = "https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=INR&apikey=43AMUJ3X4WU5W63J"


# API to get the exchange rate for a given currency pair
# write a function that takes a currency pair and returns the exchange rate
def getRate(fromCurr, toCurr):
    URLGETRATE = BASEURLGETRATE + "from_currency=" + fromCurr + "&to_currency=" + toCurr + "&apikey=" + APIKEY
    response = requests.get(URLGETRATE)
    responseJSON = json.loads(response.text)
    respRate = float(responseJSON["Realtime Currency Exchange Rate"]["5. Exchange Rate"])
   # todo: handle error if the response cannot be parsed
    return respRate

def getSharePrice(stock):
    
    shares = 1.105765
    returnUSD = 4.50

    rateUSDCAD = getRate("USD", "CAD")
    print ("USD :: CAD is", rateUSDCAD)
    returnCAD = round((returnUSD * rateUSDCAD), 2)

    rateCADINR = getRate("CAD", "INR")
    print ("CAD :: USD is", rateCADINR)

    rateUSDINR = getRate("USD", "INR")
    print ("INR :: USD is", rateUSDINR)

    print ("return ", returnUSD, "USD", " / ", returnCAD, "CAD")

    stockSymbol = "PAYTM.BSE"
    sharePrice = sharePricePaytm = getSharePrice(stockSymbol)
    print (stockSymbol, " is ", sharePrice)


    usd = round(((sharePrice * shares) / rateUSDINR), 2) - returnUSD
    print (str(usd), "USD")
    cad = round((((sharePrice * shares) / rateCADINR) - returnCAD), 2)
    print (str(cad), "CAD")
    return cad
