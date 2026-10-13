
# ASTRA MT5 BOT
# Version 0.1
# Demo / Paper Trading Only

LIVE_TRADING = False
REQUIRE_APPROVAL = True

SYMBOLS = ["EURUSD", "XAUUSD"]

def main():
    print("ASTRA MT5 BOT STARTED")
    print("Mode: DEMO / PAPER TRADING")
    print("Live trading:", LIVE_TRADING)
    print("Approval required:", REQUIRE_APPROVAL)

    for symbol in SYMBOLS:
        print("Watching symbol:", symbol)

if __name__ == "__main__":
    main()
