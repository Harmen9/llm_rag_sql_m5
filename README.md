# LLM RAG SQL M5

## Description
This tool is a proof of concept for a chatbot who will answer questions about data in a sql database.
The model should be able to query the data and come up with answers easy questions such as:
* What is the most expensive product?
* What day of the week has the highest sales?
* Which month has the lowest sales?
* Which store sells the most products?
* Which special events causes the most sales?

It uses the m5 forecasting data from Kaggle https://www.kaggle.com/competitions/m5-forecasting-accuracy.
This uses hierarchical sales data, made available by Walmart.

## Data

For more information see: https://mofc.unic.ac.cy/m5-competition/.

It used hierarchical sales data, generously made available by Walmart, starting at the item level and aggregating to that of departments, product categories and stores in three geographical areas of the US: California, Texas, and Wisconsin.

Besides the time series data, it also included explanatory variables such as price, promotions, day of the week, and special events (e.g. Super Bowl, Valentine’s Day, and Orthodox Easter) that affect sales.

The data is uploaded in respective tables:
| Original file | table name | description |
|----------|----------|----------|
|calendar.csv| calendar | Contains information about the dates on which the products are sold. |
|sales_train_validation.csv| sales | Contains the historical daily unit sales data per product and store [d_1 - d_1913] |
|sell_prices.csv |sell_prices | Contains information about the price of the products sold per store and date. |


