import yfinance as yf

"""
Borsa Class
"""

class Borsa:
    def __init__(self, label="NONE"):
        #1 - Check which market the stock belongs to
        #2 - Check if that market is open or not
        if isinstance(label, str):
            self.label = label
            self._ready = True
        else: raise Exception("Enter a valid stock label (E.g. for Gamestop Inc type \"GME\")")        
        
    def checkMarketOpening(self, market):
        if isinstance(market, str):self.market = market
        else:raise Exception("Enter a valid stock exchange (E.g. for Shanghai Stock Exchange type \"SHANGHAI\")")
        self.times = {} 
        self.markets = ["NEWYORK", "NASDAQ", "TORONTO", "JAPAN", "MEXICO", "SHANGHAI", 
        "SHENZHEN", "HONGKONG", "INDIANATIONAL", "SINGAPORE", "INDIABOMBAY", "SAUDI", 
        "KOREA", "LONDON", "FRANKFURT", "SWISS", "AMSTERDAM", "STOCKHOLM", "SAOPAULO", 
        "JOHANNESBURG", "AUSTRALIA"]
        if market in self.markets: self.market = market
        else: raise Exception("Enter a valid stock exchange (E.g. for Shanghai Stock Exchange type \"SHANGHAI\")")
        if self.market == self.markets[0]: self.times = {"opening": "14:30", "closing": "21:00"}
        elif self.market == self.markets[1]:self.times = {"opening": "14:30", "closing": "21:00"}
        elif self.market == self.markets[2]:self.times = {"opening": "14:30", "closing": "21:00"}
        elif self.market == self.markets[3]:self.times = {"opening": "00:00", "closing": "06:00"}
        elif self.market == self.markets[4]:self.times = {"opening": "14:30", "closing": "21:00"}
        elif self.market == self.markets[5]:self.times = {"opening": "01:30", "closing": "07:00"}
        elif self.market == self.markets[6]:self.times = {"opening": "01:30", "closing": "07:00"}
        elif self.market == self.markets[7]:self.times = {"opening": "01:30", "closing": "08:10"}
        elif self.market == self.markets[8]:self.times = {"opening": "03:45", "closing": "10:00"}
        elif self.market == self.markets[9]:self.times = {"opening": "00:30", "closing": "09:06"}
        elif self.market == self.markets[10]:self.times = {"opening": "03:45", "closing": "10:00"}
        elif self.market == self.markets[11]:self.times = {"opening": "07:00", "closing": "12:00"}
        elif self.market == self.markets[12]:self.times = {"opening": "00:00", "closing": "06:30"}
        elif self.market == self.markets[13]:self.times = {"opening": "08:00", "closing": "16:30"}
        elif self.market == self.markets[14]:self.times = {"opening": "08:00", "closing": "16:30"}
        elif self.market == self.markets[15]:self.times = {"opening": "08:00", "closing": "16:30"}
        elif self.market == self.markets[16]:self.times = {"opening": "08:00", "closing": "16:30"}
        elif self.market == self.markets[17]:self.times = {"opening": "08:00", "closing": "16:30"}
        elif self.market == self.markets[18]:self.times = {"opening": "08:00", "closing": "16:30"}
        elif self.market == self.markets[19]:self.times = {"opening": "12:00", "closing": "21:00"}
        elif self.market == self.markets[20]:self.times = {"opening": "07:00", "closing": "15:00"}
        elif self.market == self.markets[21]:self.times = {"opening": "00:00", "closing": "06:00"}
    
    def getStockInfo(self):
        if self._ready:
            stock = yf.Ticker(self.label)
            return {"label": self.label, 
            "exchange": stock.info["market"], 
            "price": stock.info["currentPrice"], 
            "currency": stock.info["currency"], 
            "marketcap": stock.info["marketCap"], 
            "50avg": stock.info["fiftyDayAverage"]}
        else: raise Exception("Error")
    def getMarketTimes(self):
        if self._ready:return self.times
        else: raise Exception("Error")
        
    def checkLabelValidity(self, label):
        ords= [ord(x) for x in label]
        for x in ords:
            if x > 97: raise Exception("Enter a valid stock label (E.g. for Gamestop Inc type \"GME\")")
        if isinstance(label, str):return 0 
        else: raise Exception("Enter a valid stock label (E.g. for Gamestop Inc type \"GME\")")

    def checkMarketValidity(self, market):
        if isinstance(market, str):return 0
        elif market in self.markets: return 0
        else:raise Exception("Enter a valid stock exchange (E.g. for Shanghai Stock Exchange type \"SHANGHAI\")")
"""
User Interface Functions
"""
def inputUI_1():
    print("~~~Mert's Borsa Program~~~\nEnter Stock Label: ")
    inp = input(" > ")
    return inp

def inputUI_2():
    print("~~~Mert's Borsa Program~~~\nEnter Stock Exchange: (E.g. SHANGHAI or LONDON)")
    inp = input(" > ")
    return inp

def UI():
    print("~~~Mert's Borsa Program~~~")
    l = ["Display Stock Information", "Display Market Opening & Closing Times","Display All Markets", "Observer Mode", "Select Stock Label & Exchange", "Exit Program"]
    for i, x in enumerate(l):
        print(f"{i + 1} - {x}")
    inp = input(" > ")
    return inp