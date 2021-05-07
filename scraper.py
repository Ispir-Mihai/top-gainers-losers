# Imports
import requests, bs4

# Here we store the data
top_gainers = {}
top_losers = {}

# Url of Gainers and Losers
base_url = 'https://coinmarketcap.com/gainers-losers/'

# Make a request at the base_url and store it in a varaible (res)
with requests.get(base_url) as res:

    # Initiate the BeautifulSoup on the requsted page
    soup = bs4.BeautifulSoup(res.content, 'lxml')

    # Find the Top Gainers and Top Losers tables
    top_gainers_data = soup.find('h3', text='Top Gainers').parent.find_all('tr')
    top_losers_data  = soup.find('h3', text='Top Losers').parent.find_all('tr')

    # Loop throgh the first 10 Top Gainers
    for data in top_gainers_data[1:11]:
        tds = data.find_all('td')

        # Find all the values and modify them so they can be converted to float
        price = float(tds[2].get_text().replace('$','').replace(',',''))
        change24h = float(tds[3].find('span').get_text().replace('%','').replace(',',''))
        volume24h = float(tds[4].get_text().replace('$','').replace(',',''))

        # Add the data into the Top Gainers dictionary
        top_gainers[data.find('p', class_='sc-1eb5slv-0 iJjGCS').get_text()] = { 'price' : price, 'change24h' : change24h, 'volume24h' :  volume24h }

    # Same thing like above but with Top Losers
    for data in top_losers_data[1:11]:
        tds = data.find_all('td')

        price = float(tds[2].get_text().replace('$','').replace(',',''))
        change24h = float(tds[3].find('span').get_text().replace('%','').replace(',',''))
        volume24h = float(tds[4].get_text().replace('$','').replace(',',''))

        top_losers[data.find('p', class_='sc-1eb5slv-0 iJjGCS').get_text()] = { 'price' : price, 'change24h' : change24h, 'volume24h' :  volume24h }
