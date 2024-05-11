from StockModel import *



class StockController:
    def __init__(self) -> None:
        self.model = StockModel(
            all_data=None,
            ticker=None,
            value=None,
            graphtype=None,
            from_date="2022-01-01",
            to_date="2023-12-31",
            ax=None)

    def initialize_corr(self, corr1, corr2, stock, ax):
        self.model.corr1 = corr1
        self.model.corr2 = corr2
        self.model.stock_cor = stock
        self.model.ax_corr = ax

    def get_all_data_from_ui(
            self,
            all_data,
            stock,
            value,
            graphtype,
            from_date,
            to_date,
            ax):
        """ Get all data from UI and set to StockStat class"""
        self.model.all_data = all_data
        self.model.ticker = stock
        self.model.value = value
        self.model.graphtype = graphtype
        self.model.from_date = from_date
        self.model.to_date = to_date
        self.model.ax = ax

    def load_data(self):
        return self.model.load_data()

    def plotting(self):
        """Plotting the graph"""
        return self.model.plotting()

    def describe(self):
        return self.model.compute_descriptive()

    def plotting_cor(self):
        return self.model.ploting_corr()

    def compute_coff(self):
        return self.model.compute_coefficient()

    def describe_corr(self):
        return self.model.compute_descriptive_for_corr()

    def show_distribution(self, stock, ax):
        return self.model.distribution_graph(stock, ax)

    def descriptive_distribution(self, stock):
        return self.model.descriptive_for_distribution(stock)

    def AlL_price(self, ax):
        return self.model.All_prices(ax)

    def closing_price(self, ax):
        return self.model.closing_volume(ax)

    def bar_volume(self, ax):
        return self.model.bar_volume(ax)




