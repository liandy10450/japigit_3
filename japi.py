import urllib.request

APIKEY = 'GN24I16UW66GC63Y'
#example
#URL = 'https://www.alphavantage.co/query?function=BATCH_STOCK_QUOTES&symbols=AAPL&apikey=GN24I16UW66GC63Y'

def getStockData(symbol):
    URL = 'https://www.alphavantage.co/query?function=BATCH_STOCK_QUOTES&symbols=' + symbol + '&apikey=GN24I16UW66GC63Y'    
    try:
        connection = urllib.request.urlopen(URL)
        responseString = connection.read().decode()

        return responseString
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