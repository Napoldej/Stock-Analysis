from StockModel import  *
from StockUi import *
class StockController:
    def __init__(self) -> None:
        self.stm = StockModel(all_data=None, ticker=None,
                            value=None, graphtype=None,from_date="2022-01-01",to_date= "2023-12-31",ax=None)



    def initialize_corr(self,corr1,corr2,stock,ax):
        self.stm.corr1 = corr1
        self.stm.corr2 = corr2
        self.stm.stock_cor = stock
        self.stm.ax_corr = ax

    def get_all_data_from_ui(self, all_data, stock, value, graphtype, from_date, to_date, ax):
        """ Get all data from UI and set to StockStat class"""
        self.stm.all_data = all_data
        self.stm.ticker = stock
        self.stm.value = value
        self.stm.graphtype = graphtype
        self.stm.from_date = from_date
        self.stm.to_date = to_date
        self.stm.ax = ax


    def load_data(self):
        return self.stm.load_data()


    def plotting(self):
        """Plotting the graph"""
        return self.stm.plotting()

    def describe(self):
        return self.stm.compute_descriptive()

    def plotting_cor(self):
        return self.stm.ploting_corr()

    def compute_coff(self):
        return self.stm.compute_coefficient()


    def describe_corr(self):
        return self.stm.compute_descriptive_for_corr()


    def show_distribution(self, stock,ax):
        return self.stm.distribution_graph(stock,ax)

    def descriptive_distribution(self,stock):
        return self.stm.descriptive_for_distribution(stock)


    def AlL_price(self,ax):
        return self.stm.All_prices(ax)

    def closing_price(self,ax):
        return self.stm.closing_volume(ax)

    def bar_volume(self,ax):
        return self.stm.bar_volume(ax)

