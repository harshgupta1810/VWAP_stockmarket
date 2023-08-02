## VWAP Calculator

## Introduction
This project provides a VWAP (Volume-Weighted Average Price) calculator and several related functionalities to analyze stock prices. VWAP is a popular technical indicator used by traders to understand the average price at which most trading activity has occurred over a given time period. This information can be used to identify trends, confirm trading strategies, and execute large orders more effectively.

## Table of Contents
1. [What is VWAP?](#what-is-vwap)
2. [Formula of VWAP](#formula-of-vwap)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Configuration](#configuration)
6. [Contributing](#contributing)
7. [License](#license)
8. [Acknowledgments](#acknowledgments)
9. [Documentation](#documentation)

## What is VWAP?
VWAP stands for Volume-Weighted Average Price. It is a financial indicator used to measure the average price at which a security, such as a stock, has been traded throughout a specific period, taking into account both the price and the volume of each trade. VWAP is commonly used by traders and investors to gain insights into market trends, determine trading strategies, and execute orders more efficiently.

### Calculation of VWAP
The VWAP is calculated by multiplying the price of each trade by its corresponding volume, summing up these values over a given time period (typically a trading day), and dividing by the total volume traded during that period.

### Interpretation of VWAP
The VWAP line on a chart represents the average price at which most of the trading activity has occurred. It provides a reference point to assess whether the current market price is above or below the average price.

### Uses of VWAP
1. **Mean Reversion**: One way to use VWAP is as a mean reversion strategy. If the current market price is significantly above the VWAP, it may suggest that the stock is overvalued, and a trader might consider selling or shorting it. Conversely, if the price is significantly below the VWAP, it may indicate an undervalued stock, prompting a trader to consider buying or going long.

2. **Trend Confirmation**: VWAP can also be used to confirm the direction of a trend. If the stock price is consistently trading above the VWAP, it could indicate a bullish trend, while prices trading consistently below the VWAP may signal a bearish trend. Traders may use this information to align their trades with the prevailing trend.

3. **Trading Execution**: Traders often use VWAP as a reference point for executing large orders. They aim to buy below the VWAP or sell above it to obtain a favorable average price for their trades. By splitting large orders into smaller ones and executing them gradually throughout the day, traders can minimize market impact and reduce the risk of significantly affecting the stock's price.

## Formula of VWAP
The formula for calculating VWAP is the cumulative typical price multiplied by total volume and divided by the cumulative volume. It goes as follows:
```
VWAP = [Cumulative (Price * Volume)] / [Cumulative Volume]
```
Where:
- `Cumulative (Price * Volume)`: The sum of each trade's price multiplied by its corresponding volume over a given time period.
- `Cumulative Volume`: The sum of the volumes of all trades over the same time period.

## Installation
To use this VWAP calculator, you will need Python and the matplotlib library installed on your system. Follow these steps to get started:

1. Install Python: Download and install Python from the official website: https://www.python.org/downloads/
2. Install matplotlib: Open a command prompt or terminal and run the following command:
   ```
   pip install matplotlib
   ```

## Usage
To calculate the VWAP for a given dataset, you can use the `calculate_vwap` function provided in the code. This function takes a DataFrame containing the following columns: 'High', 'Low', 'Close', 'Volume'. The VWAP values will be added as a new column 'VWAP' in the DataFrame.

Example usage:
```python
import pandas as pd
from vwap_calculator import calculate_vwap, plot_vwap

# Load your stock data into a pandas DataFrame
df = pd.read_csv('your_stock_data.csv')

# Calculate VWAP
df = calculate_vwap(df)

# Plot stock price and VWAP
plot_vwap(df)
```

## Configuration
No special configuration is required for this project.

## Contributing
If you find any issues or have suggestions for improvement, please feel free to submit a pull request or open an issue on the GitHub repository.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments
Special thanks to Harsh Gupta for creating this project.

## Documentation
For more details on the code implementation and functions, refer to the code comments and documentation in the source files.
