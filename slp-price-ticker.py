from tkinter import *
import requests
import os

from time import strftime

gas_min = 188292
gas_max = 196569

if os.environ.get('DISPLAY','') == '':
    print('no display found. Using :0.0')
    os.environ.__setitem__('DISPLAY', ':0.0')

class UpdateLabel():

    def __init__(self):
        self.w1 = Tk()
        self.w1.title("smooth-love-potion value")
        self.w1.bind('<Configure>', self.resize)
        self.w1.attributes('-fullscreen',True)   #fullscreen
        #self.w1['bg'] = "black"

        self.f1 = Frame(self.w1, bg='black', height=300, width=700)
        self.f1.pack(fill='both', expand=True)
        
        #slp value label declaration
        self.slpValue = Label(self.f1, text="", bg='black', fg='white', font = ('Helvetica', 100, 'bold',))
        self.slpValue.place(relx=0.5, rely=0.35, anchor='center', relheight=0.7, relwidth=1)

        #slp marketcap declaration
        self.slpMarketCap = Label(self.f1, text="", bg='black', fg='white', font = ('Helvetica', 30, 'bold',))
        self.slpMarketCap.place(relx=0.5, rely=0.7, anchor='n', relheight=0.1, relwidth=1)

        #slp total volume declaration
        self.slpTotalVolume = Label(self.f1, text="", bg='black', fg='white', font = ('Helvetica', 30, 'bold',))
        self.slpTotalVolume.place(relx=0.5, rely=0.8, anchor='n', relheight=0.1, relwidth=1)

        #update counter declaration
        self.timeCntr = Label(self.f1, text="", bg='black', fg='white', font = ('Helvetica', 15, 'bold'))
        self.timeCntr.place(relx=0, rely=0, anchor='nw')

        #exit window
        self.button2 = Button(self.w1, text='STOP', width=25, bg='black', fg='white', command=self.w1.destroy)
        self.button2.place(relx=0.5, rely=1, anchor='s', relheight=0.05)

        self.update_slp()
        self.updater()
        self.w1.mainloop()

    def resize(self, event):
        self.slpLblHeight = self.slpValue.winfo_height()
        self.slpLblWidth = self.slpValue.winfo_width()
        print('slp height %s width %s' % (self.slpLblHeight, self.slpLblWidth))
        self.slpValue['font'] = ('Helvetica', int(self.slpLblHeight / 2) , 'bold',)

    def update_slp(self):
        #coingecko SLP API update
        try:
            rs0 = requests.get("https://api.coingecko.com/api/v3/coins/smooth-love-potion")
            data = rs0.json()
            self.slpValue['text'] = '₱' + f"{data['market_data']['current_price']['php']:,}"
            self.slpValue['fg'] = "white"
            self.slpMarketCap['text'] = '₱' + f"{data['market_data']['market_cap']['php']:,}"
            self.slpMarketCap['fg'] = "white"
            self.slpTotalVolume['text'] = '₱' + f"{data['market_data']['total_volume']['php']:,}"
            self.slpTotalVolume['fg'] = "white"
        except:
            self.slpValue['fg'] = "red"
            self.slpMarketCap['fg'] = "red"
            self.slpTotalVolume['fg'] = "red"
            print(" slp error")
        
    def updater(self):
        self.time_str = strftime('%I:%M:%S %p')
            
        self.timeCntr['text'] = self.time_str

        if strftime('%S') == "00":
            self.update_slp()

        #update every 1 minute
        self.w1.after(1000, self.updater)
        

UL = UpdateLabel()


