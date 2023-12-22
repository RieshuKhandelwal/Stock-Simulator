# Stock Simulator

This project is a stock simulator built with the `taipy` framework. It consists of three main Python files: `stocksimulator.py`, `receiver.py`, and `sender.py`.

## stocksimulator.py

This script sets up the GUI for the stock simulator. It includes a chart that displays the min and max prices for a given stock over a range of dates. The user can input the name of the stock, as well as the min and max prices, and then run the simulation.

## receiver.py

This script sets up a server that listens for incoming data. When data is received, it updates the chart in the GUI with the new data.

## sender.py

This script sends data to the server set up in `receiver.py`. The data sent includes a random price of the stock within the min and max range, which is then displayed on the chart in the GUI. The script reads the stock name, min price, and max price from a file named `data.txt`, generates a random price within the range, and sends this data to the server every 5 seconds.

## Running the Project

To run the project, first start the server by running `receiver.py`. Then, run `stocksimulator.py` to start the GUI. Finally, run `sender.py` to start sending data to the server.

## Dependencies

This project requires the `taipy` framework and `pandas`.

## Author

This project was created by Rieshu.
