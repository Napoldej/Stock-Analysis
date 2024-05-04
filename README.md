# Stock-Analysis
## Description
* This application will analyze the top ten performing stock data by Yahoo!Finance for investors and provide the tendency and volatility of each stock using descriptive statistics and correlation. 
This helps investors decide whether they should invest or not. Additionally, the application will display essential graphs such as line, bar, and scatter plots.

## Datasource
* The Dataset of this program is provided by yahoo! Finance API [`here`](https://pypi.org/project/yfinance/)<br> that contain record of each company stock value by date-time.


## How to run
The package needed for this program, yoo can install in requirements.txt file by the command `pip install -r requirements.txt.` Then you can run the program in file [`main.py`](main.py)


## Application features
- **Showing graph and Compare attribute**: On the main page, the program will display the graph according to the user interaction.
- **Descriptive Statistics**: Show the descriptive statistics of the user's selection attributes.
- **Distribution(in progress)**: Show the distribution graph of volume.
- **DataStorytelling(in progress)** Show the line graph of open, high and low prices over the period. Additionally, the program will display the scatter plot between closing price and volume attributes
- **Attribute Relationship(in progress)**: This feature is will show the scatter plot graph and compute the coefficient correlation between the user's selection attributes.
