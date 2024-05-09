import yfinance as yf


class StockModel:
    # top 10 best performance stock in 2023
    # 1.NVDA(Nvidia)
    # 2.META(Meta Platforms)
    # 3.RCL(RoyalCaribbean)
    # 4.BLDR(Builders FirstSource)
    # 5.UBER(Uber)
    # 6.CCL(Carnival)
    # 7.AMD(Advanced Micro Devices)
    # 8.PHM(PulteGroup)
    # 9.PANW(Palo Alto Networks)
    # 10.TSLA(Tesla)
    def __init__(self, all_data, ticker ,value, graphtype,from_date, to_date, ax):
        self.all_data = all_data
        self.__ticker = ticker
        self.__value = value
        self.__graphtype = graphtype
        self.__from_date = from_date
        self.__to_date = to_date
        self.ax = ax
        self.__corr1 = None
        self.__corr2 = None
        self.__stock_cor = None
        self.__ax_corr = None

    @property
    def ticker(self):
        return self.__ticker

    @ticker.setter
    def ticker(self, ticker:str):
        self.__ticker = ticker


    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value : str):
        self.__value = value

    @property
    def graphtype(self):
        return self.__graphtype

    @graphtype.setter
    def graphtype(self,graphtype : str):
        self.__graphtype = graphtype

    @property
    def from_date(self):
        return self.__from_date

    @from_date.setter
    def from_date(self, from_date):
        self.__from_date = from_date

    @property
    def to_date(self):
        return self.__to_date

    @to_date.setter
    def to_date(self, to_date):
        self.__to_date = to_date

    @property
    def corr1(self):
        return self.__corr1

    @corr1.setter
    def corr1(self,corr1):
        self.__corr1 = corr1

    @property
    def corr2(self):
        return self.__corr2

    @corr2.setter
    def corr2(self,corr2):
        self.__corr2 = corr2

    @property
    def stock_cor(self):
        return self.__stock_cor

    @stock_cor.setter
    def stock_cor(self,stock_cor):
        self.__stock_cor = stock_cor

    @property
    def ax_corr(self):
        return self.__ax_corr

    @ax_corr.setter
    def ax_corr(self,ax_corr):
        self.__ax_corr = ax_corr


    def load_data(self):
        self.all_data = yf.download(["NVDA","META","RCL", "BLDR", "UBER", "CCL",
                                     "AMD","CCL","PHM", "AAPL", "TSLA"], start='2022-01-01', end='2023-12-31')
        self.all_data.columns = self.all_data.columns.swaplevel(0, 1)
        return self.all_data

    def plotting(self):
        """Set dataframe and Plotting the graph"""
        self.filter_data = self.all_data.loc[self.__from_date:self.__to_date]
        q1 = self.filter_data[self.ticker][self.value].quantile(0.25)
        q3 = self.filter_data[self.ticker][self.value].quantile(0.75)
        iqr = q3 - q1
        temp_df = self.filter_data[~((self.filter_data[self.ticker][self.value] < q1 - 1.5 * iqr) | (self.filter_data[self.ticker][self.value] > q3 + 1.5 * iqr))]
        temp_df.hist(column=self.ticker)
        if len(self.value) == 2:
            return temp_df[self.ticker][self.value].plot(kind=self.graphtype, xlabel='date', ylabel=f"{self.value[0]} and {self.value[1]}", title=f'{self.value[0]} vs {self.value[1]} chart of {self.ticker}', ax=self.ax, grid=True, logy=False)
        self.filter_data = self.all_data.loc[self.__from_date:self.__to_date]
        return temp_df[self.ticker][self.value].plot(kind=self.graphtype, xlabel='date', ylabel=self.value[0], title=f'{self.value[0]} chart of {self.ticker}', ax=self.ax, grid=True, logy=False)

    def compute_descriptive(self):
        filter_data = self.all_data.loc[self.__from_date:self.__to_date]
        if len(self.value) == 2:
            filter_value = filter_data[self.ticker][self.value[0]]
            filter_value1 = filter_data[self.ticker][self.value[1]]
            describe_value  = filter_value.describe()
            describe_value1 = filter_value1.describe()
            return describe_value,describe_value1
        filter_value = filter_data[self.ticker][self.value[0]]
        describe_value = filter_value.describe()
        return describe_value


    def ploting_corr(self):
        filter_data1 = self.all_data[self.stock_cor]


        return filter_data1.plot(kind = "scatter", x = self.__corr1,y = self.__corr2,xlabel = f"{self.__corr1}", ylabel = f"{self.__corr2}", ax = self.ax_corr)

    def compute_coefficient(self):

        filter_data2 = self.all_data[self.stock_cor]
        return filter_data2[self.__corr1].corr(filter_data2[self.__corr2])

    def compute_descriptive_for_corr(self):
        filter_value_corr1 = self.all_data[self.stock_cor][self.__corr1]
        filter_value_corr2 = self.all_data[self.stock_cor][self.__corr2]
        describe_1 =  filter_value_corr1.describe()
        describe_2 =  filter_value_corr2.describe()
        return describe_1,describe_2

    def distribution_graph(self,stock, ax):
        filter_data1 = self.all_data[stock]

        q1 = filter_data1["Volume"].quantile(0.25)
        q3 = filter_data1["Volume"].quantile(0.75)
        iqr = q3 - q1
        temp_df = filter_data1[~((filter_data1["Volume"] < q1 - 1.5 * iqr) | (
                    filter_data1["Volume"] > q3 + 1.5 * iqr))]

        volume_dist = temp_df["Volume"].plot(kind =  "hist",ax = ax, title = f"The volume distribution of {stock}", xlabel = "The sales of volume (in ten million)")
        return volume_dist


    def descriptive_for_distribution(self,stock):
        filter_value_descrip = self.all_data[stock]["Volume"]
        describe_volume = filter_value_descrip.describe()
        return describe_volume



    def All_prices(self,ax):
        att_list = ["Open","High","Low", "Adj Close"]
        filter_data = self.all_data["NVDA"]
        return filter_data[att_list].plot(ylabel = "Price", xlabel = "Date", title = "Stock Prices for NVDA", kind = "line", ax = ax)



    def closing_volume(self,ax):
        filter_data1 = self.all_data["NVDA"]
        return filter_data1.plot(kind = "scatter", x = "Close", y = "Volume",
                                title = "Correlation between Closing price and Volume", ax =ax)


    def bar_volume(self,ax):
        filter_data1 = self.all_data["NVDA"]

        q1 = filter_data1["Volume"].quantile(0.25)
        q3 = filter_data1["Volume"].quantile(0.75)
        iqr = q3 - q1
        temp_df = filter_data1[~((filter_data1["Volume"] < q1 - 1.5 * iqr) | (
                filter_data1["Volume"] > q3 + 1.5 * iqr))]

        return temp_df["Volume"].plot(kind = "bar",ax = ax, xlabel = "Date", title = "Volume", x= "Date", ylabel = "the Sale of Volume")








