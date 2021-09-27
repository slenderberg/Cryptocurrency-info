from scraped_currency_info import currency_table_head_list, currency_name_list, currency_symbol_list, \
    currency_price_list, currency_change_24h_list, currency_change_7d_list, currency_market_cap_list, \
    currency_volume_24h_list, currency_more_info_link_list
from tkinter import *
from table import Table
from webbrowser import open_new


def main():
    window = Tk()
    window.title("Crypto Prices")
    icon = PhotoImage(file='logo.png')
    window.iconphoto(True, icon)
    window.resizable(False, False)
    window.geometry("1095x415")
    window.config(bg='WHITE')

    Table(window, currency_table_head_list, currency_name_list, currency_symbol_list, currency_price_list,
          currency_change_24h_list, currency_change_7d_list, currency_market_cap_list, currency_volume_24h_list,
          currency_more_info_link_list)

    go_to_site = Button(window, width=64, font=('Arial', 20, 'bold'), text="CLICK HERE TO GO TO WEBSITE", bg='black',
                        fg='white')
    go_to_site.bind("<Button-1>", lambda e, url="https://coinmarketcap.com/": open_new(url))
    go_to_site.place(x=0, y=360)
    window.mainloop()


if __name__ == '__main__':
    main()
