from StockModel import  *

class StockController:
    def init(self) -> None:
        self.stm = StockModel(all_data=None, stock=None,
                            value=None, graphtype=None, ax=None)

    def get_all_data_from_ui(self, all_data, stock, value, graphtype, ax):
        """ Get all data from UI and set to StockStat class"""
        self.stm.all_data = all_data
        self.stm.ticker = stock
        self.stm.value = value
        self.stm.graphtype = graphtype
        self.stm.ax = ax

    def load_data(self):
        """Load data from yahoo finance"""
        return self.stm.load_data()

    def plotting(self):
        """Plotting the graph"""
        return self.stm.plotting()

