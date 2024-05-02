from StockModel import  *

class StockController:
    def __init__(self) -> None:
        self.stm = StockModel(all_data=None, ticker=None,
                            value=None, graphtype=None,from_date="2022-01-01",to_date= "2023-12-31",ax=None)

    def get_all_data_from_ui(self, all_data, stock, value, graphtype,from_date, to_date, ax):
        """ Get all data from UI and set to StockStat class"""
        self.stm.all_data = all_data
        self.stm.ticker = stock
        self.stm.value = value
        self.stm.graphtype = graphtype
        self.stm.from_date = from_date
        self.stm.to_date = to_date
        self.stm.ax = ax

    def load_data(self):
        """Load data from yahoo finance"""
        return self.stm.load_data()

    def plotting(self):
        """Plotting the graph"""
        return self.stm.plotting()

