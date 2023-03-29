# Company-Data-Scraper
I developed this script using Selenium to scrape financial data for a list of companies from moneycontrol.com. The inspiration for this project came from my dad, who wanted me to obtain the share prices of a set of companies.

To make the process of collecting data easier and more efficient, I decided to automate it using Python. The script takes in a text file containing a list of company names, searches for each company on Google to navigate to the moneycontrol website, and extracts relevant information such as registered office, registras, and stock prices. It then stores the data in a list of dictionaries, creates a Pandas DataFrame from the list of dictionaries, and exports it to a CSV file with the current date as the file name.

This script uses Selenium to scrape financial data for a list of companies from moneycontrol.com. The script takes in a file containing a list of company names and searches for each company on Google to navigate to the moneycontrol website. It then extracts relevant information such as registered office, registras, and stock prices from the website and stores the data in a list of dictionaries. Finally, it creates a Pandas DataFrame from the list of dictionaries and exports it to a CSV file with the current date as the file name.

## Requirements

Python 3.x, 
Selenium,
Pandas.  

### Installation. 

Install Python 3.x from the official website: https://www.python.org/downloads/ <br>
Install Selenium using pip: pip install selenium <br>
Install Pandas using pip: pip install pandas <br>

## Usage

Create a text file with the name company_name_set.txt in the same directory as the script.
Add a list of company names to the text file, with each company name on a new line.
Run the script in a Python environment. The script will scrape data for each company in the text file and export it to a CSV file with the current date as the file name.
The script will print the extracted data for each company to the console as a dictionary.

## Disclaimer

This script is for educational purposes only. Scraping data from websites without their permission may violate their terms of service. It is the responsibility of the user to ensure they have the legal right to scrape data from any website before doing so.
