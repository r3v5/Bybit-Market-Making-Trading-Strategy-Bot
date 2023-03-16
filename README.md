# Introduction

The main idea of this project is creating a market-making bot that trades a specific cryptocurrency on an exchange, using the Bybit testnet API to receive real-time market data. The app was done by [**Ian Miller**](https://t.me/J0anix)

# Brief explanation of understanding key concepts

### What is Market-neutral trading?

- Market neutral refers to a type of investment strategy employed by investment managers that seek to profit from both increasing and decreasing prices in the financial markets.
- Known as a market-neutral strategy, the investment selections seek to avoid significant losses, as the long and short positions serve as a hedge to one another.
- Market-neutral strategies are often employed by hedge funds as their investment objective is absolute returns rather than relative returns.
- The two main types of market-neutral strategies that fund managers employ are fundamental arbitrage and statistical arbitrage.
- Market-neutral strategies have one of the lowest positive correlations to the market because they place specific bets on asset price convergences while hedging away the general market risk.

### What is Market making?

- A market maker is an individual participant or member firm of an exchange that buys and sells securities for its own account.
- Market makers provide the market with liquidity and depth while profiting from the difference in the bid-ask spread.
- Brokerage houses are the most common types of market makers, providing purchase and sale solutions for investors.
- Market makers are compensated for the risk of holding assets because asset's value may decline between its purchase and sale to another buyer.
- While brokers compete against one another, specialists post bids and asks and ensure they are reported accurately.

### What is funding rates on centralized exchanges?

- Funding rates are periodic payments either to traders that are long or short based on the difference between perpetual contract markets and spot prices. Therefore, depending on open positions, traders will either pay or receive funding.
- Crypto funding rates prevent lasting divergence in the price of both markets.
- In periods of high volatility, the price between the perpetual contract and the mark price may diverge. In such instances, the premium increases or decreases accordingly.
- A large spread equates to a high premium. Conversely, a low premium indicates a narrow spread between the two prices.
- When the funding rate is positive, the price of the perpetual contract is higher than the mark price, thus, traders who are long pay for short positions. Conversely, a negative funding rate indicates that perpetual prices are below the mark price, which means that short positions pay for longs.
- Essentially, funding rates are designed to encourage traders to take positions that keep perpetual contract prices line in with spot markets.
- As such, inefficiencies between perpetual contracts and mark prices are arbitraged away, resulting in a narrow spread between the two prices. Although extreme volatility may cause occasional spikes in funding rates, arbitrageurs will seize these opportunities quickly. Thus, funding rates eventually reverts to its mean.

### What is cash-and-carry-trades?

- A cash-and-carry trade is an arbitrage strategy that profits off the mispricing between the underlying asset and its corresponding derivative.
- A cash-and-carry trade is usually executed by entering a long position in an asset while simultaneously selling the associated derivative.
- Specifically, this is done by going short the market via a futures or options contract.
- An investor identifies two securities that are mispriced with respect to each other; for instance, the spot crude price and crude futures price, which presents an [arbitrage](https://www.investopedia.com/terms/a/arbitrage.asp) opportunity.
- The investor must first purchase spot crude and sell a crude futures contract. Then, they hold (or "carry") spot crude until the crude futures contract expires, at which time the investor delivers the spot crude.
- Regardless of what the delivery price is, a profit is only assured if the purchase price of spot crude _plus_ the [cost of carry](https://www.investopedia.com/terms/c/costofcarry.asp) is less than the price at which the crude futures contract was initially sold.

### Example of a Cash-and-Carry Trade

Assume an asset currently trades at $100 while the one-month futures contract is priced at $104. In addition, monthly [carrying costs](https://www.investopedia.com/terms/c/carrying-costs.asp)—such as storage, insurance, and financing—for this asset is equal to $2. In this case, the trader would buy the asset (open a long position) at $100, and simultaneously sell the one-month futures contract (initiate a short position) at $104.
The cost to buy and hold the asset is $102, but the investor has already locked in a sale at $104. The trader would then carry the asset until the expiration date of the futures contract and deliver it against the contract, thereby ensuring an arbitrage profit of $2.

# Strategy

### Proof of concept

https://www.wikijob.co.uk/trading/forex/market-making
I have implemented grid strategy for market-making
In this case, a market maker places limit orders throughout the book, of increasing size, around a moving average of the price, and then leaves them there.

The idea is that the price will 'walk through' the orders throughout the day, earning the spreads between buys and sells.

As the order sizes get larger with the spreads, this strategy has the **martingale effect** – it effectively doubles down as prices deviate from the average price.

Unlike Stoikov, as the orders are further apart, fills happen less often, but the spreads (and hence profits) are larger.

In this strategy, the most important thing is **calculating the average price**.

The best way to do this is:

- A moving average of prices
- A moving average of prices + a jump function (a function that resets the average after a sudden spike)
- The current best bid-offer price, reset periodically (as per the high-frequency algorithm described above)
- Looking at the prices on other exchanges/related instruments (sometimes called **statistical arbitrage**)

# Technology stack

- Python 3.10.6
- Virtualenv
- [ccxt](https://github.com/ccxt/ccxt)
- [Bybit testnet](https://testnet.bybit.com/app/terms-service/information)

# Get started

- Go to [Bybit testnet](https://testnet.bybit.com/app/terms-service/information) and create `Api key` and `Secret key`
  ![Image](https://github.com/turnMeUpSon/Market-Making-Trading-Strategy-Test/blob/main/Screenshot%20from%202023-03-14%2009-44-01.png)
- `git clone https://github.com/turnMeUpSon/Market-Making-Trading-Strategy-Test.git`
- `pip3 install -r requirements.txt`
- Paste `Api key` and `Secret key` from Bybit testnet account into your `config.py` like this: `API_KEY =  "your_api_key"`, `SECRET_KEY = "your_secret_key"`
- Claim test USDT on Bybit testnet exchange
- In order to start the bot, you should run this command in your terminal: `python market_maker_bot.py`
- Then check your `Current orders` and `Trade History` in Spot trading in https://testnet.bybit.com/app/terms-service/information

# Results

## 2023-03-13
![Image](https://github.com/turnMeUpSon/Market-Making-Trading-Strategy-Test/blob/main/Screenshot%20from%202023-03-13%2016-54-46.png)
## 2023-03-14
![Image](https://github.com/turnMeUpSon/Bybit-Market-Making-Trading-Strategy-Bot/blob/main/Screenshot%20from%202023-03-14%2013-00-38.png)
It's the fact that we bought cheaper and sold more expensive

# My contacts

- [Telegram](https://t.me/J0anix)
- milleryan2003@gmail.com
