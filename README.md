# Lotto Max Analyzer

## Click [here](https://lottomax-analyser-fe.herokuapp.com/) to view the live app.

This project is a simple tool for analyzing the results of the Canadian Lotto Max lottery. The project consists of two main components:

1. A data scraper that extracts the winning numbers for each Lotto Max draw from the official website.
2. An analysis script that reads in the winning numbers data and performs some basic statistical analysis on the numbers.

## Setup

To use this tool, you'll need to install the following packages:

- Python 3
- BeautifulSoup
- numpy
- matplotlib

You can install these packages using pip:
pip install -r requirements.txt


## Usage

To use this tool, first run the `predictor.py` script to extract the winning numbers data. This will generate the following four files:

### 1. DrawsDataWithDates.txt

This file contains the winning numbers for each draw date, and the data is formatted as follows:

[date] [winning numbers]


For example:

23-Feb-2022 [5, 8, 10, 13, 32, 36, 46]
26-Feb-2022 [1, 6, 10, 18, 23, 36, 48]
01-Mar-2022 [12, 15, 17, 25, 32, 37, 49]
...


### 2. DrawsGraph.png

This graph shows the Lotto Max draw numbers for each draw date. The x-axis represents the draw dates and the y-axis represents the numbers. Each data point represents a draw, and the marker 'o' is used to indicate each data point. The data points are annotated with their respective winning numbers. The graph is saved as a PNG file named 'drawfig.png'.

### 3. DrawSumGraph.png

This graph shows the sum of the Lotto Max draw numbers for each draw date. The x-axis represents the draw dates and the y-axis represents the sum of the numbers. Each data point represents a draw, and the marker 'o' is used to indicate each data point. The graph is saved as a PNG file named 'sumfig.png'. 

### 4. NumberFrequencyGraph.png

This graph shows the frequency of each number in the winning numbers data. The x-axis represents the numbers and the y-axis represents the frequency. The graph is saved as a PNG file named 'numfreq.png'.

All four files - DrawGraph.png, DrawSumGraph.png, NumberFrequencyGraph.png, and DrawsDataWithDates.txt - are saved in the same directory as the Python script.

## License

This project is licensed under the MIT License. See the [LICENSE](https://github.com/greeshmasunil10/LottoMaxAnalyser/blob/main/LICENSE) file for details.

## Acknowledgments

- The Lotto Max data is sourced from the [lottomaxnumbers.com](https://www.lottomaxnumbers.com/).

