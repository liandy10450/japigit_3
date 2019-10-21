import urllib.request

APIKEY = 'GN24I16UW66GC63Y'
#example
#URL = 'https://www.alphavantage.co/query?function=BATCH_STOCK_QUOTES&symbols=AAPL&apikey=GN24I16UW66GC63Y'

def getStockData(symbol):
    URL = 'https://www.alphavantage.co/query?function=BATCH_STOCK_QUOTES&symbols=' + symbol + '&apikey=' + APIKEY   
    try:
        connection = urllib.request.urlopen(URL)
        responseString = connection.read().decode()
        substrString = responseString.find('price')
        return responseString[substrString+9:substrString+15]
    except:    
        return "not found"

def main():
    outFile = open('japi.out', 'w')
    #infinitely asks user for stock symbol until quit
    while 1:    
        userInput = input("Please input stock symbol or 'quit' to exit: ").upper()
        if userInput != "QUIT":
            currPrice = 'The current price of {} is: {}\n'.format(userInput, getStockData(userInput))
            print(currPrice)
            outFile.write(currPrice)
        else:
            break
main()           