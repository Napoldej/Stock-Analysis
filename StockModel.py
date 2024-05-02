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
    def init(self, all_data, stock , value, graphtype, ax):
        self.all_data = all_data
        self.stock = stock
        self.value = value
        self.graphtype = graphtype
        self.ax = ax

    @property
    def stock(self):
        return self.stock

    @stock.setter
    def stock(self, stock:str):
        self.stock = stock


    @property
    def value(self):
        return self.value

    @value.setter
    def value(self, value : str):
        self.value = value

    @property
    def graphtype(self):
        return self.graphtype

    @graphtype.setter
    def graphtype(self,graphtype : str):
        self.__graphtype = graphtype



    def load_data(self):
        self.all_data = yf.download(["NVDA","META","RCL", "BLDR", "UBER", "CCL",
                                     "AMD","CCL","PHM", "PAWN", "TSLA"], start='2022-01-01', end='2023-12-31')

        self.all_data.columns = self.all_data.columns.swaplevel(0, 1)
        return self.all_data

    def plotting(self):
        """Set dataframe and Plotting the graph"""
        if len(self.value) == 2:
            return self.all_data[self.stock][self.value].plot(kind=self.graphtype, xlabel='date', ylabel=f"{self.value[0]} and {self.value[1]}", title=f'{self.value[0]} vs {self.value[1]} chart of {self.stock}', ax=self.ax, grid=True, logy=False)
        return self.all_data[self.stock][self.value].plot(kind=self.graphtype, xlabel='date', ylabel=self.value[0], title=f'{self.value[0]} chart of {self.stock}', ax=self.ax, grid=True, logy=False)