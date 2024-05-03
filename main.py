from StockUi import StockUI
from Stockcontroller import StockController

if __name__ == "__main__":
    controller = StockController()
    main = StockUI(controller)
    main.run()

