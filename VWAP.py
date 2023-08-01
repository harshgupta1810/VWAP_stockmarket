'''
Calculation of VWAP: The VWAP is calculated by multiplying the price of each trade by its corresponding volume, summing up these values over a given time period (typically a trading day), and dividing by the total volume traded during that period.

Interpretation: The VWAP line on a chart represents the average price at which most of the trading activity has occurred. It provides a reference point to assess whether the current market price is above or below the average price.

Mean Reversion: One way to use VWAP is as a mean reversion strategy. If the current market price is significantly above the VWAP, it may suggest that the stock is overvalued, and a trader might consider selling or shorting it. Conversely, if the price is significantly below the VWAP, it may indicate an undervalued stock, prompting a trader to consider buying or going long.

Trend Confirmation: VWAP can also be used to confirm the direction of a trend. If the stock price is consistently trading above the VWAP, it could indicate a bullish trend, while prices trading consistently below the VWAP may signal a bearish trend. Traders may use this information to align their trades with the prevailing trend.

Trading Execution: Traders often use VWAP as a reference point for executing large orders. They aim to buy below the VWAP or sell above it to obtain a favorable average price for their trades. By splitting large orders into smaller ones and executing them gradually throughout the day, traders can minimize market impact and reduce the risk of significantly affecting the stock's price.
'''


'''
Formula of VWAP
The formula for calculating VWAP is the cumulative typical price multiplied by total volume and divided by the cumulative volume. It goes as follows:

VWAP = [Cumulative (Price * Volume)]/[Cumulative Volume]
'''
from matplotlib import pyplot as plt


def calculate_vwap(df):
    cumulative_volume = []
    previous_cumulative_volume = 0

    # Calculate the Typical Price =  (High + Low + Close)/3
    df['Typical_Price'] = (df['Close'] + df['High'] + df['Low']) / 3

    # Calculate the Volume_Typical_Price  = (Typical Price * Volume)
    df['Volume_Typical_Price'] = df['Typical_Price'] * df['Volume']

    # Calculate the cumulative sum of volume_Typical_Price
    df['Cumulative_Volume_Typical_Price'] = df['Volume_Typical_Price'].cumsum()

    # Calculate the cumulative sum of volume
    cumulative_volume = df['Volume'].cumsum()

    # VWAP = Cumulative (Volume * Typical Price) / Cumulative Volume
    df['VWAP'] = df['Cumulative_Volume_Typical_Price'] / cumulative_volume

    return df



def plot_vwap(df):
    # Plot stock price and VWAP
    plt.plot(df.index, df['Close'], label='Stock Price')
    plt.plot(df.index, df['VWAP'], label='VWAP')
    plt.title('Stock Price and Volume-Weighted Average Price (VWAP)')
    plt.xlabel('Time')
    plt.ylabel('Price')
    plt.legend()
    plt.grid(True)
    plt.show()


def calculate_mean_reversion(df):
    # Calculate VWAP
    df['VWAP'] = df['Volume_Typical_Price'] / df['Volume']

    # Calculate mean reversion
    df['Mean_Reversion'] = df['Close'] - df['VWAP']

    # Determine overvalued, undervalued, or neutral
    df['Mean_Reversion_Status'] = df['Mean_Reversion'].apply(lambda x: 'Overvalued' if x > 0.2 else ('Undervalued' if x < -0.2 else 'Neutral'))

    return df


def calculate_trend_confirmation(df):
    # Calculate trend confirmation
    df['Trend_Confirmation'] = df.apply(lambda row: 'Bullish' if row['Close'] > row['VWAP'] else ('Bearish' if row['Close'] < row['VWAP'] else 'Neutral'), axis=1)

    return df


def calculate_trading_execution(df):
    # Calculate trading execution
    df['Trading_Execution'] = df.apply(lambda row: 'Buy' if row['Close'] < row['VWAP'] else ('Sell' if row['Close'] > row['VWAP'] else 'Neutral'), axis=1)

    return df
