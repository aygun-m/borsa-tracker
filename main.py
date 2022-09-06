
from os import system
system("pip3 install -r requirements.txt")
from time import sleep
from core import Borsa, inputUI_2, inputUI_1, UI
on = True
while on:
    system("clear")
    try:
        validBorsa = Borsa()
        inp_1 = inputUI_1()
        validBorsa.checkLabelValidity(inp_1)
        while True:
            system("clear")
            b = Borsa(inp_1)
            userInput = UI()
            if userInput == "1":
                system("clear")
                stockInfo = b.getStockInfo()
                label = stockInfo["label"]
                exchange = stockInfo["exchange"]
                price = stockInfo["price"]
                currency = stockInfo["currency"]
                marketcap = stockInfo["marketcap"]
                fiftyavg = stockInfo["50avg"]
                print("~~~Mert's Borsa Program~~~")
                print(f"Label: {label}")
                print(f"Exchange: {exchange}")
                print(f"Price: {price}")
                print(f"Currency: {currency}")
                print(f"Market Cap: {marketcap}")
                print(f"50-Day Average: {fiftyavg}")
                input("~~~Go Back - Press Enter~~~")
            elif userInput == "2":
                system("clear")
                inp_2 = inputUI_2()
                validBorsa.checkMarketValidity(inp_2)
                b.checkMarketOpening(inp_2)
                times = b.getMarketTimes()
                opens = times["opening"]
                closes = times["closing"]
                print(f"{b.market} Exchange\nOpen at {opens} GMT+0\nClosed at {closes} GMT+0")
                input("~~~Go Back - Press Enter~~~")
                
            elif userInput == "3":
                inp_2 = inputUI_2()
                validBorsa.checkMarketValidity(inp_2)
                b.checkMarketOpening(inp_2)
                for x in b.markets:print(x)
                input("~~~Go Back - Press Enter~~~")
            elif userInput == "4":
                totalTime = 300
                stockInfo = b.getStockInfo()
                system("clear")
                while totalTime > 0:
                    totalTime = totalTime - 5
                    print("~~~Mert's Borsa Program~~~")
                    label = stockInfo["label"]
                    price = stockInfo["price"]
                    currency = stockInfo["currency"]
                    marketcap = stockInfo["marketcap"]
                    print(f"Data will refresh in {totalTime} seconds")
                    print(f"{label}: {price} {currency}")
                    print(f"Marketcap: {marketcap}")
                    sleep(5)
                    system("clear")
            elif userInput == "5":
                break 
            elif userInput == "6":
                print("Quitting...")
                exit()
            else:
                print("\nUnknown Option")
                sleep(0.5)
    except KeyboardInterrupt as e:
        print("\nExiting...")
        sleep(0.5)
        system("clear")
        break
