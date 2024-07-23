# Amazon Product Price Tracker

This project monitors and records the price of a specific Amazon product using Selenium for web automation and BeautifulSoup for HTML parsing. Data is saved into a CSV file and updated continuously.

## Prerequisites

- Python 3.x
- pip (Python package installer)
- Safari WebDriver

## Install Libraries

Install the required libraries using pip

## Usage
Clone the Repository:
git clone https://github.com/yourusername/amazon-product-price-tracker.git
cd amazon-product-price-tracker

## Run the Script:
- Update the script with the correct path to your CSV file and the URL of the Amazon product you want to track.
- Run the script
  
## Functionality
Set up WebDriver: Initializes the Safari WebDriver.
Connect to Website: Navigates to the specified Amazon product page.
Fetch and Parse Web Page: Fetches the HTML content and parses it using BeautifulSoup.
Extract Product Information: Extracts the product title and price from the parsed HTML content.
Save Data to CSV: Saves the extracted data (title, price, date) into a CSV file. If the file already exists, it appends the new data.
Automate Price Checking: Continuously checks the product price at specified intervals and updates the CSV file with the latest data.

## Additional Information
The script checks the price every 3600 seconds. You can adjust this interval as needed.
Ensure the WebDriver is properly configured and the necessary drivers are installed for your browser.
