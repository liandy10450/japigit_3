import urlib.request

APIKEY = 'GN24I16UW66GC63Y'
URL = 'https://www.alphavantage.co/query?function=BATCH_STOCK_QUOTES&symbols=AAPL&apikey=GN24I16UW66GC63Y'

def getStockData(symbol):
    try:
        print
    return "not found"

def main():
    outFile = open('japi.out', 'w')
    #infinitely asks user for stock symbol until quit
    while 1:    
        userInput = input("Please input stock symbol or 'quit' to exit").upper()
        if userInput != "QUIT":
            currPrice = 'The current price of {} is:{}\n'.format(userInput, getStockData(userInput))
            print(currPrice)
            outFile.write(currPrice)
        else:
            break
main()           