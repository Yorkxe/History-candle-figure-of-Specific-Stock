import time
import tkinter as tk
from tkinter import ttk #Adding Combobox in tkinter
from selenium import webdriver #Open the Parser
from selenium.webdriver.common.by import By #Finding the element
from selenium.webdriver.common.keys import Keys #Enter key
from selenium.webdriver.support.select import Select #Combobox Selection
from selenium.webdriver.chrome.options import Options   # Hide Chrome Parser
import mplfinance as mpf
import pandas as pd

url = 'https://www.twse.com.tw/zh/trading/historical/stock-day.html'
year = [i for i in range(2023, 2009, -1)]
month = [i for i in range(1, 13)]

#Limit the value input in enter grip in tkinter
def validate(P):
    if str.isdigit(P) or P == '':
        return True
    else:
        return False
#Button Event in tkinter
def button_event():
    if enter.get() == '':
        tk.messagebox.showerror('message', 'Please enter a number')
    elif int(enter.get()) <= 0:
        tk.messagebox.showerror('message', 'Please enter a positive number')
    else:
        global Year, Month, Serial
        Year = combo1.get()
        Month = combo2.get()
        Serial = enter.get()
        root.destroy()
      
#Ending nutton in tkinter
def ending():
    global switch 
    switch = 0
    root.destroy()

#Selenium Function
def getting_data(Year, Month, Serial):
    global result
    result = []
    chrome_options = Options()                              
    chrome_options.add_argument('--headless')               
    driver = webdriver.Chrome()
    driver = webdriver.Chrome(chrome_options) 
    driver.get(url) # Go to TWSE Website
    
    time.sleep(3)
    Stock_name = driver.find_element(By.NAME, "stockNo")
    selectA = driver.find_element(By.NAME, "yy")
    selectB = driver.find_element(By.NAME, "mm")
    select = Select(selectA)
    
    select.select_by_value(Year)
    time.sleep(2)
    
    select = Select(selectB)
    select.select_by_value(Month)
    time.sleep(2)
    
    Stock_name.send_keys(Serial)
    
    button = driver.find_element(By.CSS_SELECTOR, "#form > div > div.groups > div.submit > button")
    button.send_keys(Keys.ENTER)
    
    time.sleep(2)
    try:
        #Getting the data we want
        data = driver.find_element(By.XPATH, """//*[@id="reports"]/div[2]/div[2]/table/tbody""").text
        temp = ""
        for i in data:
            if i != " " and i != "\n":
                temp += i
            else:
                result.append(temp)
                temp = ""
        result.append(temp)
        Plot_Candlestickchart()
    except:
        Error = tk.Tk()
        Error.title('No Such Data!!')
        Error.geometry('350x100')
        mylabel = tk.Label(Error, text = '                           ', height = 3)
        mylabel.grid(row = 0, column = 1)
        mylabel = tk.Label(Error, text = 'No Such Data!!', height = 3)
        mylabel.grid(row = 0, column = 2)
         
def Plot_Candlestickchart():
    global result, Serial
    num = len(result) // 9
    data = [[0] * 6 for _ in range(num)]
    for i, j in enumerate(result):
        if i % 9 == 0:
            j = str( int(j[0:3]) + 1911)+ '-' + j[4:6] + '-' + j[7:9]
            data[i // 9][i % 9] = j
        elif i % 9 == 1:
            j = int(j.replace(',', ''))
            j /= 1000
            data[i // 9][i % 9] = j
        elif i % 9 in [3, 4, 5, 6]:
            data[i // 9][i % 9 - 1] = float(j.replace(',', ''))
    data_plot = pd.DataFrame(data, columns=['Date','Volume', 'Open', 'High', 'Low', 'Close'])
    data_plot.index = pd.DatetimeIndex(data_plot['Date'])
    mpf.plot(data_plot, type='candle', style='yahoo', mav=(5, 10), \
title = Serial + '\'s candle figure', volume = True,
ylabel_lower='Shares')
    
switch = 1
while 1:
    root = tk.Tk()
    root.title('History candle figure of Specific Stock')
    root.geometry('900x100')
    
    mylabel = tk.Label(root, text = 'Select the date value', height = 1)
    mylabel.grid(row = 0, column = 0)
    
    #Combo box for year/month selection
    combo1 = ttk.Combobox(root, values = year, height = 5)
    combo1.grid(row = 0, column = 1)
    combo1.current(0)
    
    combo2 = ttk.Combobox(root, values = month, height = 5)
    combo2.grid(row = 0, column = 2)
    combo2.current(0)
    
    #Value enter
    vcmd = (root.register(validate), '%P')
    enter = tk.Entry(root, validate = 'key', validatecommand = vcmd)
    enter.grid(row = 0, column = 3)
    
    #Enter button
    mybutton = tk.Button(root, text = 'Enter', command = button_event, width = 5, height = 1)
    mybutton.grid(row = 0, column = 4)
    
    mybutton = tk.Button(root, text = 'End', command = ending, bg="red", fg="black", width = 10, height = 2)
    mybutton.grid(row = 10, column = 2)

    root.attributes('-topmost', True)
    root.update()
    root.attributes('-topmost', False)
    
    root.mainloop()
    
    if switch:
        getting_data(Year, Month, Serial)
    else:
        break

