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


    def load_data(self):
        self.all_data = yf.download(["NVDA","META","RCL", "BLDR", "UBER", "CCL",
                                     "AMD","CCL","PHM", "AAPL", "TSLA"], start='2022-01-01', end='2023-12-31')
        self.all_data.columns = self.all_data.columns.swaplevel(0, 1)
        return self.all_data

    def plotting(self):
        """Set dataframe and Plotting the graph"""
        if len(self.value) == 2:
            self.filter_data = self.all_data.loc[self.__from_date:self.__to_date]
            return self.filter_data[self.ticker][self.value].plot(kind=self.graphtype, xlabel='date', ylabel=f"{self.value[0]} and {self.value[1]}", title=f'{self.value[0]} vs {self.value[1]} chart of {self.ticker}', ax=self.ax, grid=True, logy=False)
        self.filter_data = self.all_data.loc[self.__from_date:self.__to_date]
        return self.filter_data[self.ticker][self.value].plot(kind=self.graphtype, xlabel='date', ylabel=self.value[0], title=f'{self.value[0]} chart of {self.ticker}', ax=self.ax, grid=True, logy=False)

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










