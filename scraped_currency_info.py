from bs4 import BeautifulSoup
import requests


def get_table_heads(table, head_list):
    for h in table.thead.tr:
        head_list.append(h.text)
    indexes = [0, 9, 10, 8]
    for index in sorted(indexes, reverse=True):
        del head_list[index]
    head_list.append('Link')


def get_currency_name_symbol_and_price(crypto_list, name_list, symbol_list, price_list):
    crypto_count = 0
    for crypto in crypto_list:
        if crypto_count <= 9:
            name_and_symbol = crypto.find('a', {'class': 'cmc-link'}).find_all('div', {
                'class': 'sc-16r8icm-0 sc-1teo54s-1 dNOTPP'})
            prices = crypto.find_all('div', {'class': 'sc-131di3y-0 cLgOOr'})
            for j in name_and_symbol:
                crypto_name = j.find('p', {'class': 'sc-1eb5slv-0 iworPT'})
                crypto_symbol = j.find('p', {'class': 'sc-1eb5slv-0 gGIpIK coin-item-symbol'})

                name_list.append(crypto_name.text)
                symbol_list.append(crypto_symbol.text)
            for p in prices:
                price_list.append(p.text)
        crypto_count += 1


def get_change_percent(crypto_list, list_24h, list_7d):
    num = 2
    for i in range(0, len(crypto_list)):
        changes = crypto_list[i].find_all('td', {'style': 'text-align:right'})
        increase_dict = {'class': 'sc-15yy2pl-0 kAXKAX'}
        decrease_dict = {'class': 'sc-15yy2pl-0 hzgCfk'}

        for change in changes:
            if change.find('span', increase_dict) is not None:
                if num % 2 == 0:
                    if change.find('span', increase_dict).find('span', {'class': 'icon-Caret-up'}) is not None:
                        list_24h.append(f"+{change.find('span', increase_dict).text}")
                    elif change.find('span', increase_dict).find('span', {'class': 'icon-Caret-down'}) is not None:
                        list_24h.append(f"-{change.find('span', increase_dict).text}")
                else:
                    if change.find('span', increase_dict).find('span', {'class': 'icon-Caret-up'}) is not None:
                        list_7d.append(f"+{change.find('span', increase_dict).text}")
                    elif change.find('span', increase_dict).find('span', {'class': 'icon-Caret-down'}) is not None:
                        list_7d.append(f"-{change.find('span', increase_dict).text}")
            if change.find('span', decrease_dict) is not None:
                if num % 2 == 0:
                    if change.find('span', decrease_dict).find('span', {'class': 'icon-Caret-up'}) is not None:
                        list_24h.append(f"+{change.find('span', decrease_dict).text}")
                    elif change.find('span', decrease_dict).find('span', {'class': 'icon-Caret-down'}) is not None:
                        list_24h.append(f"-{change.find('span', decrease_dict).text}")
                else:
                    if change.find('span', decrease_dict).find('span', {'class': 'icon-Caret-up'}) is not None:
                        list_7d.append(f"+{change.find('span', decrease_dict).text}")
                    elif change.find('span', decrease_dict).find('span', {'class': 'icon-Caret-down'}) is not None:
                        list_7d.append(f"-{change.find('span', decrease_dict).text}")
            num += 1


def get_volume_and_market_cap(crypto_list, marketcap_list, volume_list):
    for crypto in range(10):
        market_cap = crypto_list[crypto].find('span', {'class': 'sc-1ow4cwt-0 iosgXe'})
        volume_24h = crypto_list[crypto].find('div', {'class': 'sc-16r8icm-0 j3nwcd-0 cRcnjD'}).find('p', {
            'class': 'sc-1eb5slv-0 etpvrL'})

        marketcap_list.append(market_cap.text)
        volume_list.append(volume_24h.text)


def get_more_info_link(crypto_list, more_info_link_list):
    count = 0
    for crypto in crypto_list:
        if count <= 10:
            link = crypto.find('a', {'class': 'cmc-link'})
            more_info_link_list.append(f"https://coinmarketcap.com{link['href']}")
            count += 1


# scraping and parsing html source code
url = "https://coinmarketcap.com/"
html_text = requests.get(url).text
soup = BeautifulSoup(html_text, 'lxml')

# scraping html code of the table
currency_div = soup.find('div', {'class': 'h7vnx2-1 bFzXgL'})
currency_table = currency_div.find('table', {'class': 'h7vnx2-2 czTsgW cmc-table'})

# scraping headings
currency_table_head_list = []
get_table_heads(currency_table, currency_table_head_list)

# scraping currency info into a list
cryptos = currency_div.find('tbody').find_all('tr')

# scraping the currency name ,symbol and price
currency_name_list = []
currency_symbol_list = []
currency_price_list = []
get_currency_name_symbol_and_price(cryptos, currency_name_list, currency_symbol_list, currency_price_list)

# scraping the change in price in percent in the last 24h and 7 days
currency_change_24h_list = []
currency_change_7d_list = []
get_change_percent(cryptos, currency_change_24h_list, currency_change_7d_list)

# scraping market cap and volume
currency_market_cap_list = []
currency_volume_24h_list = []
get_volume_and_market_cap(cryptos, currency_market_cap_list, currency_volume_24h_list)

# scraping more info link
currency_more_info_link_list = []
get_more_info_link(cryptos, currency_more_info_link_list)

