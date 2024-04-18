# Portugal KPI Report

## Goal
This project intends to generate automatically a modern-looking report of changes in Portuguese Tourism and Economy Indicators, so that stakeholders can get a quick overview of latest trends.

## How it works
1. Obtains recent data from INE and Banco de Portugal for select indicators
2. Generates plots and tables for each indicator, identifying changes vs. same period last year and vs. previous month.
3. Summarizes and reports largest variations for a quick overview
4. Sends e-mail to stakeholders letting them know that the report was generated

## Techonologies used
* Python - obtaining, preparing and plotting data, sending email
* Quarto - report rendering and publishing
* GitHub Pages - publishing the report as a web page for easy viewing
* GitHub Actions - scheduling, automatic rendering and publishing

## Next steps
* Writing blog post explaining how to replicate the set up
* Adding more indicators
* Longer description of current indicators
* Correlation between indicators
* Forecasting future amounts
