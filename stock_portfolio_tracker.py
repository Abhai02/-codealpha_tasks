import yfinance as yf

class StockPortfolio:
    def __init__(self):
        self.portfolio = {}
    
    def add_stock(self, symbol, shares):
        if symbol in self.portfolio:
            self.portfolio[symbol] += shares
        else:
            self.portfolio[symbol] = shares
        print(f"Added {shares} shares of {symbol} to portfolio.")
    
    def remove_stock(self, symbol, shares):
        if symbol in self.portfolio:
            if shares >= self.portfolio[symbol]:
                del self.portfolio[symbol]
                print(f"Removed all shares of {symbol} from portfolio.")
            else:
                self.portfolio[symbol] -= shares
                print(f"Removed {shares} shares of {symbol} from portfolio.")
        else:
            print(f"Stock {symbol} not found in portfolio.")
    
    def get_stock_price(self, symbol):
        try:
            stock = yf.Ticker(symbol)
            return stock.history(period="1d")["Close"].iloc[-1]
        except Exception as e:
            print(f"Error fetching price for {symbol}: {e}")
            return None
    
    def view_portfolio(self):
        if not self.portfolio:
            print("Portfolio is empty.")
            return
        
        print("\nCurrent Portfolio:")
        total_value = 0
        for symbol, shares in self.portfolio.items():
            price = self.get_stock_price(symbol)
            if price is not None:
                value = price * shares
                total_value += value
                print(f"{symbol}: {shares} shares @ ${price:.2f} each = ${value:.2f}")
        
        print(f"\nTotal Portfolio Value: ${total_value:.2f}")

if __name__ == "__main__":
    tracker = StockPortfolio()
    while True:
        print("\nOptions: add, remove, view, exit")
        action = input("Enter action: ").strip().lower()
        if action == "add":
            symbol = input("Enter stock symbol: ").upper()
            shares = int(input("Enter number of shares: "))
            tracker.add_stock(symbol, shares)
        elif action == "remove":
            symbol = input("Enter stock symbol: ").upper()
            shares = int(input("Enter number of shares to remove: "))
            tracker.remove_stock(symbol, shares)
        elif action == "view":
            tracker.view_portfolio()
        elif action == "exit":
            break
        else:
            print("Invalid action. Please try again.")
