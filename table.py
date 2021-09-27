from tkinter import *
from webbrowser import open_new


class Table:
    def make_entry(self, root, h, name, symbol, data, width, fg, column):
        if not name and not symbol:
            self.e = Entry(root, width=width, fg=fg, font=('Arial', 17, 'bold'))

            self.e.grid(row=h + 1, column=column)
            self.e.insert(END, data[h])
            self.e.config(state='readonly', justify=CENTER)
        else:
            self.e = Entry(root, width=width, fg=fg, font=('Arial', 17, 'bold'))

            self.e.grid(row=h + 1, column=column)
            self.e.insert(END, name[h])
            self.e.insert(END, ' - ')
            self.e.insert(END, symbol[h])
            self.e.config(state='readonly', justify=CENTER)

    def __init__(self, root, heads, names, symbols, prices, changes_24h, changes_7d, market_cap, volume_24h, more_info):
        width_list = [2, 18, 10, 8, 8, 10, 20, 6]
        # code for creating table
        for head in range(8):
            self.e = Entry(root, width=width_list[head], fg='black', font=('Arial', 17, 'bold'), justify=CENTER)

            self.e.grid(row=0, column=head)
            self.e.insert(END, heads[head])
            self.e.config(state='readonly')

        for h in range(10):
            col = 0
            self.e = Entry(root, width=2, fg='black', font=('Arial', 18, 'bold'), justify=CENTER)

            self.e.grid(row=h + 1, column=col)
            self.e.insert(END, h + 1)
            self.e.config(state='readonly')

            col += 1
            self.make_entry(root, h, names, symbols, False, 18, '#bd00fc', col)

            col += 1
            self.make_entry(root, h, False, False, prices, 10, 'Blue', col)

            col += 1
            if changes_24h[h][0] == '-':
                self.make_entry(root, h, False, False, changes_24h, 8, 'red', col)
            else:
                self.make_entry(root, h, False, False, changes_24h, 8, 'green', col)
            col += 1
            if changes_7d[h][0] == '-':
                self.make_entry(root, h, False, False, changes_7d, 8, 'red', col)
            else:
                self.make_entry(root, h, False, False, changes_7d, 8, 'green', col)

            col += 1
            self.make_entry(root, h, False, False, market_cap, 10, 'blue', col)

            col += 1
            self.make_entry(root, h, False, False, volume_24h, 20, 'blue', col)

            col += 1
        for a in range(10):
            self.b = Button(root, width=7, fg='blue', font=('Arial', 13, 'bold'), text="More Info")
            self.b.bind("<Button-1>", lambda e, url=more_info[a]: open_new(url))
            self.b.grid(row=a + 1, column=7)
